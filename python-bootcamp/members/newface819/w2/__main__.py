from datetime import date
from pathlib import Path

from .io_utils import load_tasks

# __main__.py -> w2 -> newface819 -> members -> python-bootcamp
SAMPLE = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"


def main() -> None:
    """
    Load the sample CSV and print one line per task.
    """
    today = date.today()
    for i, task in enumerate(load_tasks(SAMPLE), start=1):
        print(f"{i}. {task.title}: importance {task.importance}, {task.effort_h} h, "
              f"due {task.deadline} ({task.days_left(today)} days left)")


if __name__ == "__main__":
    main()
