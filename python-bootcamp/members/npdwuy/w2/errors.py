from members.npdwuy.w2.models import Task


class InfeasiblePlan(Exception):
    """The tasks need more hours than are available."""

    def __init__(self, needed_h: float, available_h: float):
        super().__init__(needed_h, available_h)
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return (f"plan needs {self.needed_h:g} h but only {self.available_h:g} h are available "
                f"({self.needed_h - self.available_h:g} h short)")


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the tasks' total effort is more than available_h."""
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed, available_h)
