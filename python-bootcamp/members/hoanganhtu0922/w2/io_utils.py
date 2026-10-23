"""W2-2 Load tasks from CSV and save to JSON."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read tasks from a CSV file with header title,importance,effort_h,deadline.

    Header row counts as line 1. Each data row is line 2, 3, …
    A bad row (wrong type, importance outside 1-5, bad date) raises
    ValueError("line N: <reason>").
    """
    tasks: list[Task] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            try:
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])
                task = Task(
                    title=row["title"],
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            except (ValueError, KeyError) as exc:
                raise ValueError(f"line {line_num}: {exc}") from exc
            tasks.append(task)
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Serialize tasks to a JSON file. Dates are stored as ISO strings."""
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
