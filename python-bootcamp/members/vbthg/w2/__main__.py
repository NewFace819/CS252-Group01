"""Load and print the instructor's sample tasks with python -m."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Locate the sample relative to this package and print each task."""
    sample = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    for task in load_tasks(sample):
        print(f"{task.title}: importance={task.importance}, effort={task.effort_h:g} h, "
              f"deadline={task.deadline.isoformat()}")


if __name__ == "__main__":
    main()
