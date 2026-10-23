"""W2-3 Custom exception for infeasible study plans."""

from __future__ import annotations

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when total task effort exceeds available hours.

    Attributes:
        needed_h:    total effort required by all tasks.
        available_h: hours the student has free.
    """

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Plan requires {self.needed_h:.1f} h "
            f"but only {self.available_h:.1f} h are available "
            f"({self.needed_h - self.available_h:.1f} h short)."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the total effort exceeds available hours.

    Does nothing if the plan fits within the given time budget.
    """
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)
