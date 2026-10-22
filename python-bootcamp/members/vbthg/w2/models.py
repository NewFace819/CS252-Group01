"""The individual W2 task model, independent of the team's shared contract."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with an importance from 1 to 5 and a due date."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject importance values outside the integer scale."""
        if type(self.importance) is not int or not 1 <= self.importance <= 5:
            raise ValueError("importance must be an integer from 1 to 5")

    def days_left(self, today: date) -> int:
        """Return days until the deadline; due and overdue tasks return zero."""
        return max((self.deadline - today).days, 0)
