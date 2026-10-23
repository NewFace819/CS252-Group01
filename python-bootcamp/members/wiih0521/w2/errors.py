"""W2-3: Custom exceptions and feasibility checks for the study planner."""

from __future__ import annotations

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when the total effort exceeds the available hours.

    Attributes
    ----------
    needed_h : float
        Sum of ``effort_h`` across all tasks.
    available_h : float
        Hours the student actually has.
    """

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Need {needed_h} h but only {available_h} h available"
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise :class:`InfeasiblePlan` if total effort exceeds *available_h*.

    Parameters
    ----------
    tasks : list[Task]
        The tasks to check.
    available_h : float
        Total hours the student can spend.

    Raises
    ------
    InfeasiblePlan
        If ``sum(t.effort_h for t in tasks) > available_h``.
    """
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed_h=needed, available_h=available_h)
