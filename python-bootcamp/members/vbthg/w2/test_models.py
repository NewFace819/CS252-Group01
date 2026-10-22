"""Boundary checks for the individual task model."""

from datetime import date

import pytest

from members.vbthg.w2.models import Task


@pytest.mark.parametrize("importance", [1, 5])
def test_importance_endpoints(importance):
    assert Task("Study", importance, 1.0, date(2026, 10, 30)).importance == importance


@pytest.mark.parametrize("importance", [0, 6, -1, 1.5, True, "3", None])
def test_invalid_importance(importance):
    with pytest.raises(ValueError, match="importance"):
        Task("Study", importance, 1.0, date(2026, 10, 30))


@pytest.mark.parametrize("today, expected", [
    (date(2026, 2, 28), 2),
    (date(2026, 3, 2), 0),
    (date(2026, 3, 3), 0),
])
def test_days_left_across_month_boundary(today, expected):
    assert Task("Study", 3, 1.0, date(2026, 3, 2)).days_left(today) == expected
