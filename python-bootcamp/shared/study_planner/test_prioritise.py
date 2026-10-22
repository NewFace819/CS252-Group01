from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise, score

TODAY = date(2026, 10, 26)


def task(title, importance, deadline, effort_h=1.0):
    return Task(title, importance, effort_h, deadline)


def titles(tasks):
    return [t.title for t in tasks]


def test_sample_csv_order():
    # samples/tasks.csv: Assignment 4/1 = 4.0 beats DS exam 5/4 = 1.25 (the W3-3 example).
    tasks = [task("DS exam", 5, date(2026, 10, 30), 6), task("Assignment", 4, date(2026, 10, 27), 1.5)]
    assert titles(prioritise(tasks, TODAY)) == ["Assignment", "DS exam"]


def test_score():
    assert score(task("a", 4, date(2026, 10, 28)), TODAY) == 2.0
    assert score(task("b", 3, date(2026, 10, 26)), TODAY) == 3.0   # due today: 1 day
    assert score(task("c", 3, date(2026, 10, 20)), TODAY) == 3.0   # overdue: 1 day


def test_overdue_counts_as_one_day():
    tasks = [task("late", 2, date(2026, 10, 1)), task("soon", 3, date(2026, 10, 28))]
    # late: 2 / 1 = 2.0, soon: 3 / 2 = 1.5
    assert titles(prioritise(tasks, TODAY)) == ["late", "soon"]


def test_tie_goes_to_earlier_deadline():
    # 2 / 2 = 1.0 and 4 / 4 = 1.0
    tasks = [task("later", 4, date(2026, 10, 30)), task("earlier", 2, date(2026, 10, 28))]
    assert titles(prioritise(tasks, TODAY)) == ["earlier", "later"]


def test_full_tie_keeps_input_order():
    d = date(2026, 10, 29)
    tasks = [task("x", 3, d), task("y", 3, d), task("z", 3, d)]
    assert titles(prioritise(tasks, TODAY)) == ["x", "y", "z"]


def test_returns_new_list_and_leaves_input_alone():
    tasks = [task("low", 1, date(2026, 11, 20)), task("high", 5, date(2026, 10, 27))]
    before = list(tasks)
    result = prioritise(tasks, TODAY)
    assert result is not tasks
    assert tasks == before
    assert titles(result) == ["high", "low"]


def test_empty_and_single():
    assert prioritise([], TODAY) == []
    only = task("only", 3, date(2026, 10, 30))
    assert prioritise([only], TODAY) == [only]
