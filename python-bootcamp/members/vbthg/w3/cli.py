"""Plan a limited study session using the individual W2 CSV loader and model."""

import argparse
import logging
import sys
from datetime import date
from math import fsum, isfinite
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task

LOGGER = logging.getLogger(__name__)


def format_plan(tasks: list[Task], hours: float, today: date) -> str:
    """Prioritise by importance/days left, then allocate a partial session.

    Due and overdue tasks use one day as the denominator. Ties use the earlier
    deadline, then input order. The final task can receive a partial allocation;
    the displayed total is the time allocated, not the requested budget.
    """
    if not isfinite(hours) or hours < 0:
        raise ValueError("hours must be finite and nonnegative")
    ordered = sorted(tasks, key=lambda task: (
        -task.importance / max(task.days_left(today), 1), task.deadline,
    ))
    remaining = hours
    blocks: list[tuple[str, float]] = []
    for task in ordered:
        if remaining <= 0:
            break
        allocated = min(task.effort_h, remaining)
        if allocated > 0:
            blocks.append((task.title, allocated))
            remaining -= allocated
    if not blocks:
        return "Nothing planned."
    total = fsum(allocated for _, allocated in blocks)
    lines = [f"Tonight ({total:.1f} h):"]
    for index, (title, allocated) in enumerate(blocks, start=1):
        lines.append(f"  {index}. {title} ...... {allocated:g} h")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Print a study plan; report file/data errors with exit code 1."""
    parser = argparse.ArgumentParser(description="Plan a study session from a task CSV.")
    parser.add_argument("csv", type=Path, help="task CSV with the W2 header")
    parser.add_argument("--hours", type=float, required=True, help="available study hours")
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="YYYY-MM-DD")
    args = parser.parse_args(argv)
    try:
        plan = format_plan(load_tasks(args.csv), args.hours, args.today or date.today())
    except (OSError, ValueError, UnicodeError) as error:
        LOGGER.error("Cannot create plan: %s", error)
        return 1
    print(plan)
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(message)s", stream=sys.stderr)
    raise SystemExit(main())
