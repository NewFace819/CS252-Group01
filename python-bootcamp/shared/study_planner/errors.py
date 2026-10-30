"""T-W3 (THA Anh): the InfeasiblePlan error and a feasibility check for the planner.

Mirrors members/hoanganhtu0922/w2/errors.py (W2-3); members/ is not importable from
shared/, so the class lives here for the team code.
"""

from __future__ import annotations

from shared.contract import Task


class InfeasiblePlan(Exception):
    """Raised when total task effort exceeds the available hours.

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
    """Raise InfeasiblePlan if the total effort exceeds the available hours."""
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)
