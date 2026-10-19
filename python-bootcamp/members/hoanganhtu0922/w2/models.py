"""W2-1 Task dataclass with deadline and days_left helper."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A study task with priority metadata and a hard deadline."""

    title: str
    importance: int  # 1-5
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError(f"importance must be 1-5, got {self.importance}")

    def days_left(self, today: date) -> int:
        """Return days remaining until deadline; never negative."""
        return max(0, (self.deadline - today).days)
