"""Command line entry point: python -m shared.study_planner samples/tasks.csv --hours 2

Exit code 0 on success, 1 on a user error (message on stderr), 2 on bad arguments.
By default a plan that cannot fit every task is cut off at the hours available;
with --strict it fails with InfeasiblePlan instead.
"""
import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.errors import InfeasiblePlan, check_feasible
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def _fail(message: str) -> None:
    """Print an error message to stderr and exit with code 1."""
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main(argv: list[str] | None = None) -> None:
    """Chain parse_csv -> prioritise -> allocate -> render and print the plan."""
    parser = argparse.ArgumentParser(prog="study_planner", description="Plan tonight's study time.")
    parser.add_argument("csv", type=Path)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="YYYY-MM-DD")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail if the tasks do not all fit in --hours",
    )
    args = parser.parse_args(argv)

    try:
        text = args.csv.read_text(encoding="utf-8")
    except FileNotFoundError:
        _fail(f"file not found: {args.csv}")
    except OSError as exc:
        _fail(f"cannot read {args.csv}: {exc.strerror or exc}")
    if not text.strip():
        _fail(f"file is empty: {args.csv}")

    try:
        tasks = parse_csv(args.csv)
    except ValueError as exc:
        _fail(f"invalid CSV: {exc}")
    if not tasks:
        _fail(f"no tasks in {args.csv}")

    if args.strict:
        try:
            check_feasible(tasks, args.hours)
        except InfeasiblePlan as exc:
            _fail(str(exc))

    print(render(allocate(prioritise(tasks, args.today or date.today()), args.hours)))


if __name__ == "__main__":
    main()
