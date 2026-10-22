"""Check feasibility boundaries and actionable exception details."""

from datetime import date

import pytest

from members.vbthg.w2.errors import InfeasiblePlan, check_feasible
from members.vbthg.w2.models import Task


def test_infeasible_plan_exposes_both_totals():
    tasks = [Task("A", 3, 1.5, date(2026, 10, 30)), Task("B", 2, 2, date(2026, 10, 30))]
    with pytest.raises(InfeasiblePlan) as caught:
        check_feasible(tasks, 2)
    assert caught.value.needed_h == 3.5
    assert caught.value.available_h == 2
    assert str(caught.value) == "Plan needs 3.5 h, but only 2 h are available."


@pytest.mark.parametrize("budget", [1.5, 2])
def test_exact_or_surplus_budget(budget):
    assert check_feasible([Task("A", 3, 1.5, date(2026, 10, 30))], budget) is None


def test_no_tasks_need_no_hours():
    assert check_feasible([], 0) is None


def test_zero_budget_rejects_positive_effort():
    with pytest.raises(InfeasiblePlan):
        check_feasible([Task("A", 3, 0.5, date(2026, 10, 30))], 0)


def test_repeated_fractional_efforts_fit_budget():
    tasks = [Task(str(i), 3, 0.1, date(2026, 10, 30)) for i in range(30)]
    assert check_feasible(tasks, 3) is None
