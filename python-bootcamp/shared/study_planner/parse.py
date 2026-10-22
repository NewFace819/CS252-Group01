"""T-W2 (Member 2 — Đỗ Huy): Parse a CSV file into a list of Task objects.

Reads a CSV with the header ``title,importance,effort_h,deadline``
(deadline as YYYY-MM-DD).  A bad row — including ``importance`` outside 1–5 —
raises ``ValueError("line N: ...")`` with the header counted as line 1.
"""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

from shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    """Read *path* and return a list of :class:`Task` objects.

    Parameters
    ----------
    path : str | Path
        Path to a CSV file with columns
        ``title,importance,effort_h,deadline``.

    Returns
    -------
    list[Task]
        One ``Task`` per valid data row.

    Raises
    ------
    ValueError
        If a data row cannot be converted.  The message starts with the
        1-based line number (header = line 1).
    """
    tasks: list[Task] = []
    expected_header = ["title", "importance", "effort_h", "deadline"]
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != expected_header:
            raise ValueError(f"line 1: header must be {','.join(expected_header)}")
        for line_no, row in enumerate(reader, start=2):
            try:
                importance = int(row["importance"])
                if not 1 <= importance <= 5:
                    raise ValueError(
                        f"importance must be between 1 and 5, got {importance}"
                    )
                task = Task(
                    title=row["title"],
                    importance=importance,
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
            except (ValueError, KeyError) as exc:
                msg = f"line {line_no}: {exc}"
                raise ValueError(msg) from exc
            tasks.append(task)
    return tasks
