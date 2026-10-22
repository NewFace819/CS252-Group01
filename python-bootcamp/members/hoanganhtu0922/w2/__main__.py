"""W2-5 Entry point: python -m members.hoanganhtu0922.w2

Loads the sample CSV and prints each task.
"""

from pathlib import Path

from .io_utils import load_tasks

_SAMPLES = Path(__file__).parent.parent.parent.parent / "samples" / "tasks.csv"


def main() -> None:
    tasks = load_tasks(_SAMPLES)
    print(f"Loaded {len(tasks)} task(s) from {_SAMPLES.name}:\n")
    for task in tasks:
        print(
            f"  {task.title}"
            f"  |  importance={task.importance}"
            f"  |  effort={task.effort_h}h"
            f"  |  deadline={task.deadline}"
        )


if __name__ == "__main__":
    main()
