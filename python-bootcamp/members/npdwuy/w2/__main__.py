"""Run from python-bootcamp/: python -m members.npdwuy.w2"""
from pathlib import Path

from members.npdwuy.w2.io_utils import load_tasks

SAMPLE = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    """Load samples/tasks.csv and print one line per task."""
    tasks = load_tasks(SAMPLE)
    print(f"{len(tasks)} tasks from {SAMPLE.name}:")
    for i, t in enumerate(tasks, start=1):
        print(f"  {i}. {t.title} (importance {t.importance}, {t.effort_h:g} h, due {t.deadline})")


if __name__ == "__main__":
    main()
