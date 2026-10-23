"""W2-1: Task model for the study-planner domain."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with priority, estimated effort and a hard deadline.

    Parameters
    ----------
    title : str
        Short description of the task.
    importance : int
        Priority from 1 (low) to 5 (high).
    effort_h : float
        Estimated hours of work.
    deadline : date
        The day the task must be finished.

    Raises
    ------
    ValueError
        If *importance* is not in the 1–5 range.
    """

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError(
                f"importance must be between 1 and 5, got {self.importance}"
            )

    def days_left(self, today: date) -> int:
        """Return the number of days until the deadline, floored at 0."""
        delta = (self.deadline - today).days
        return max(0, delta)
