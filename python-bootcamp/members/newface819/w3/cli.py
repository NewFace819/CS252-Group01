import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main(argv: list[str] | None = None) -> int:
    """
    Print tonight's study plan for a tasks CSV. Return the exit code:
    0 on success, 1 if the file is missing or invalid.
    """
    parser = argparse.ArgumentParser(description="Plan tonight's study time.")
    parser.add_argument("csv", type=Path, help="tasks CSV (title,importance,effort_h,deadline)")
    parser.add_argument("--hours", type=float, required=True, help="hours available tonight")
    parser.add_argument("--today", type=date.fromisoformat, default=None,
                        help="YYYY-MM-DD (default: today)")
    args = parser.parse_args(argv)
    try:
        tasks = parse_csv(args.csv)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(render(allocate(prioritise(tasks, args.today or date.today()), args.hours)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
