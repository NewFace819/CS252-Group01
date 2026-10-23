"""W2-5: Run ``python -m members.wiih0521.w2`` to demo the study-planner I/O.

Loads the sample CSV and prints the tasks.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from .io_utils import load_tasks

SAMPLE_CSV = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    """Load tasks.csv from the samples folder and display them."""
    if not SAMPLE_CSV.exists():
        print(f"Error: sample file not found: {SAMPLE_CSV}", file=sys.stderr)
        sys.exit(1)

    tasks = load_tasks(SAMPLE_CSV)
    today = date.today()

    print(f"{'Title':<20} {'Imp':>3} {'Effort':>7} {'Deadline':>12} {'Days left':>10}")
    print("-" * 56)
    for t in tasks:
        print(
            f"{t.title:<20} {t.importance:>3} {t.effort_h:>7.1f} "
            f"{t.deadline.isoformat():>12} {t.days_left(today):>10}"
        )


if __name__ == "__main__":
    main()
