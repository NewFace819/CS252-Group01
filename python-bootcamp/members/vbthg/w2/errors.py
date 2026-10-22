"""Report when the requested study workload exceeds the available time."""

from math import fsum

from .models import Task


class InfeasiblePlan(Exception):
    """A plan requires more study hours than are available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        return (f"Plan needs {self.needed_h:g} h, "
                f"but only {self.available_h:g} h are available.")


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when total effort exceeds the supplied budget."""
    needed_h = fsum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
