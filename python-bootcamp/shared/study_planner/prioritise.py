from datetime import date

from shared.contract import Task


def score(task: Task, today: date) -> float:
    """importance / days left, where an overdue or due-today task counts as 1 day left."""
    days_left = (task.deadline - today).days
    return task.importance / max(days_left, 1)


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Return a new list, highest score first; ties go to the earlier deadline.

    sorted() is stable, so tasks with the same score and deadline keep their input
    order, and the input list is not changed.
    """
    return sorted(tasks, key=lambda t: (-score(t, today), t.deadline))
