"""Command line entry point: python -m shared.study_planner samples/tasks.csv --hours 2"""
import argparse
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main(argv: list[str] | None = None) -> None:
    """Chain parse_csv -> prioritise -> allocate -> render and print the plan."""
    parser = argparse.ArgumentParser(prog="study_planner", description="Plan tonight's study time.")
    parser.add_argument("csv", type=Path)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="YYYY-MM-DD")
    args = parser.parse_args(argv)
    tasks = parse_csv(args.csv)
    print(render(allocate(prioritise(tasks, args.today or date.today()), args.hours)))


if __name__ == "__main__":
    main()
