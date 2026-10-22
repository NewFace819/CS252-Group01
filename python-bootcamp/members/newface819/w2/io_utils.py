import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task

HEADER = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path: str | Path) -> list[Task]:
    """
    Read tasks from a CSV file with the header title,importance,effort_h,deadline.
    Raise ValueError with the line number if the header or a row is invalid.
    """
    tasks = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            raise ValueError(f"line 1: the header must be {','.join(HEADER)}")
        for row in reader:
            try:
                tasks.append(Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                ))
            except (ValueError, TypeError) as e:
                raise ValueError(f"line {reader.line_num}: {e}") from e
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """
    Write the tasks to a JSON file as a list of objects.
    Deadlines are written as YYYY-MM-DD strings.
    """
    data = [{**asdict(task), "deadline": task.deadline.isoformat()} for task in tasks]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
