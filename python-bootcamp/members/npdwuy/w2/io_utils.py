import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from members.npdwuy.w2.models import Task


def load_tasks(path) -> list[Task]:
    """Read tasks from a CSV with header title,importance,effort_h,deadline.

    A bad row raises ValueError naming its line; the header is line 1.
    """
    tasks = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line, row in enumerate(reader, start=2):
            try:
                tasks.append(Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                ))
            except (KeyError, TypeError, AttributeError, ValueError) as e:
                raise ValueError(f"line {line}: {e}") from e
    return tasks


def save_json(tasks: list[Task], path) -> None:
    """Write the tasks as a JSON list, with each deadline as YYYY-MM-DD."""
    data = []
    for t in tasks:
        d = asdict(t)
        d["deadline"] = t.deadline.isoformat()
        data.append(d)
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
