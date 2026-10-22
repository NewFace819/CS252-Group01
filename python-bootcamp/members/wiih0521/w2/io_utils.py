"""W2-2: CSV / JSON I/O utilities for Task objects."""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read a CSV file and return a list of Task objects.

    The CSV must have a header row with columns:
    ``title,importance,effort_h,deadline``.

    Parameters
    ----------
    path : str | Path
        Path to the CSV file.

    Returns
    -------
    list[Task]
        Parsed tasks.

    Raises
    ------
    ValueError
        If a data row cannot be converted (includes the 1-based line number).
    """
    tasks: list[Task] = []
    expected_header = ["title", "importance", "effort_h", "deadline"]
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != expected_header:
            raise ValueError(f"line 1: header must be {','.join(expected_header)}")
        for line_no, row in enumerate(reader, start=2):  # header is line 1
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (ValueError, KeyError) as exc:
                msg = f"line {line_no}: {exc}"
                raise ValueError(msg) from exc
            tasks.append(task)
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Serialise a list of Tasks to a JSON file.

    Each task becomes a dict with keys matching the dataclass fields;
    ``deadline`` is stored as an ISO-8601 string.

    Parameters
    ----------
    tasks : list[Task]
        Tasks to serialise.
    path : str | Path
        Destination file path.
    """
    records = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    Path(path).write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
