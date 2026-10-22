from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """
    A piece of study work: a title, an importance from 1 to 5,
    the hours it needs and its deadline.
    """
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """
        Return the number of days from today to the deadline.
        Return 0 if the deadline has already passed.
        """
        return max((self.deadline - today).days, 0)
