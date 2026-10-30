"""W3-3: plan tonight's study time from a CSV of tasks.

Run from python-bootcamp/:
    python -m members.npdwuy.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26

Exit code 0 on success, 1 for a missing or bad file, 2 for bad arguments (argparse).
"""
import argparse
import math
import sys
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def hours(text: str) -> float:
    """argparse type for --hours: a finite number that is not negative."""
    try:
        h = float(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a number: {text!r}") from None
    if not math.isfinite(h) or h < 0:
        raise argparse.ArgumentTypeError(f"must be a number >= 0, got {text!r}")
    return h


def build_parser() -> argparse.ArgumentParser:
    """The command line: a CSV path, --hours and an optional --today."""
    parser = argparse.ArgumentParser(prog="python -m members.npdwuy.w3.cli",
                                     description="Plan tonight's study time.")
    parser.add_argument("csv", help="CSV with header title,importance,effort_h,deadline")
    parser.add_argument("--hours", type=hours, required=True, help="hours free tonight")
    parser.add_argument("--today", type=date.fromisoformat, default=None, metavar="YYYY-MM-DD",
                        help="date to plan from (default: today)")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Print the plan and return the exit code; errors go to stderr."""
    args = build_parser().parse_args(argv)
    try:
        tasks = parse_csv(args.csv)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"error: cannot read {args.csv}: {e.strerror or e}", file=sys.stderr)
        return 1
    except ValueError as e:  # a bad row, or a file that is not UTF-8
        print(f"error: bad CSV {args.csv}: {e}", file=sys.stderr)
        return 1
    today = args.today or date.today()
    print(render(allocate(prioritise(tasks, today), args.hours)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
