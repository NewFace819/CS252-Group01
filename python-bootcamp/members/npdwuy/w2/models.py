"""W2-1: the Task dataclass."""
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """One study task: like a C++ struct, but __init__ and __repr__ come for free."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Reject an importance outside 1-5 with ValueError."""
        if not 1 <= self.importance <= 5:
            raise ValueError(f"importance must be 1-5, got {self.importance}")

    def days_left(self, today: date) -> int:
        """Days from today until the deadline, never below 0."""
        return max((self.deadline - today).days, 0)
