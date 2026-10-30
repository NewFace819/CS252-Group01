"""W3-3: Command-line interface for the study planner."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

from .dates import parse_due


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the study planner CLI."""
    parser = argparse.ArgumentParser(
        description="Study planner CLI: schedule and allocate tasks for tonight.",
    )
    parser.add_argument(
        "csv_path",
        type=str,
        help="Path to the tasks CSV file.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours tonight.",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date (ISO format 'YYYY-MM-DD' or relative like 'today'). Default: today.",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Entry point for the CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    path = Path(args.csv_path)
    if not path.is_file():
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        sys.exit(1)

    reference_today = date.today()
    if args.today:
        try:
            today_date = parse_due(args.today, reference_today)
        except ValueError:
            try:
                today_date = date.fromisoformat(args.today)
            except ValueError as exc:
                print(f"Error: invalid --today date: {exc}", file=sys.stderr)
                sys.exit(1)
    else:
        today_date = reference_today

    try:
        tasks = parse_csv(path)
        ordered = prioritise(tasks, today_date)
        blocks = allocate(ordered, args.hours)
        output = render(blocks)
        print(output)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
