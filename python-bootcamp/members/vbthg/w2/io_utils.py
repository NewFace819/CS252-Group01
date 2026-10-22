"""Read validated task CSV rows and export JSON with ISO date strings."""

import csv
import json
from dataclasses import asdict
from datetime import date
from math import isfinite
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load the four-column CSV; invalid records name their starting file line.

    The header is line 1. Titles must be nonempty, effort finite and nonnegative,
    and deadlines use YYYY-MM-DD. Header-only files represent an empty task list.
    Filesystem errors retain their original exception types.
    """
    tasks = []
    with open(path, encoding="utf-8-sig", newline="") as source:
        reader = csv.reader(source, strict=True)
        line = 1
        try:
            if next(reader, None) != ["title", "importance", "effort_h", "deadline"]:
                raise ValueError("expected header title,importance,effort_h,deadline")
            while True:
                line = reader.line_num + 1
                row = next(reader, None)
                if row is None:
                    break
                if len(row) != 4:
                    raise ValueError("expected exactly four columns")
                title, importance, effort, deadline = (value.strip() for value in row)
                if not title:
                    raise ValueError("title must not be empty")
                effort_h = float(effort)
                if not isfinite(effort_h) or effort_h < 0:
                    raise ValueError("effort_h must be finite and nonnegative")
                due = date.fromisoformat(deadline)
                if due.isoformat() != deadline:
                    raise ValueError("deadline must use YYYY-MM-DD")
                tasks.append(Task(title, int(importance), effort_h, due))
        except (ValueError, csv.Error) as error:
            raise ValueError(f"line {line}: {error}") from error
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Write all task fields as UTF-8 JSON; serialize deadlines as ISO dates."""
    records = [{**asdict(task), "deadline": task.deadline.isoformat()} for task in tasks]
    text = json.dumps(records, ensure_ascii=False, indent=2, allow_nan=False)
    Path(path).write_text(text + "\n", encoding="utf-8")
