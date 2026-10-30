"""W3-3 Command-line study planner.

Usage (from python-bootcamp/):
    python -m members.hoanganhtu0922.w3.cli tasks.csv --hours 2 --today 2026-10-26
"""

from __future__ import annotations

import argparse
import sys
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

from ..w2.io_utils import load_tasks


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the planner CLI."""
    parser = argparse.ArgumentParser(prog="cli", description="Plan tonight's study session.")
    parser.add_argument("path", help="CSV file: title,importance,effort_h,deadline")
    parser.add_argument("--hours", type=float, required=True, help="hours available tonight")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="reference date (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return the process exit code."""
    args = build_parser().parse_args(argv)
    today = args.today or date.today()

    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: invalid CSV: {exc}", file=sys.stderr)
        return 1

    print(render(allocate(prioritise(tasks, today), args.hours)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
