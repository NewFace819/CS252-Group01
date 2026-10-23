"""Allocation tests use only shared data objects, without sibling modules."""

from dataclasses import asdict
from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def test_sample_plan_partially_fills_last_task():
    assignment = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    exam = Task("DS exam", 5, 6, date(2026, 10, 30))
    assert allocate([assignment, exam], 2) == [Block(assignment, 1.5), Block(exam, 0.5)]


def test_empty_tasks():
    assert allocate([], 2) == []


@pytest.mark.parametrize("hours", [0, -1, -0.5])
def test_nonpositive_budget(hours):
    assert allocate([Task("Study", 3, 1, date(2026, 10, 30))], hours) == []


def test_budget_smaller_than_first_task():
    first = Task("First", 1, 3, date(2026, 10, 30))
    second = Task("Second", 5, 1, date(2026, 10, 27))
    assert allocate([first, second], 0.5) == [Block(first, 0.5)]


def test_exact_budget_does_not_add_trailing_block():
    first = Task("First", 1, 1.5, date(2026, 10, 30))
    second = Task("Second", 5, 1, date(2026, 10, 27))
    assert allocate([first, second], 1.5) == [Block(first, 1.5)]


def test_surplus_budget_does_not_overallocate():
    tasks = [Task("A", 3, 1, date(2026, 10, 30)), Task("B", 2, 0.5, date(2026, 10, 30))]
    assert allocate(tasks, 10) == [Block(tasks[0], 1), Block(tasks[1], 0.5)]


def test_order_identity_and_input_fields_are_preserved():
    first = Task("Later, less important", 1, 1, date(2026, 11, 30))
    second = Task("Earlier, more important", 5, 1, date(2026, 10, 27))
    tasks = [first, second]
    before = [asdict(task) for task in tasks]
    blocks = allocate(tasks, 1.5)
    assert blocks == [Block(first, 1), Block(second, 0.5)]
    assert blocks[0].task is first and blocks[1].task is second
    assert tasks[0] is first and tasks[1] is second
    assert [asdict(task) for task in tasks] == before


def test_zero_effort_follows_contract_minimum_rule():
    done = Task("Done", 3, 0, date(2026, 10, 30))
    pending = Task("Pending", 3, 2, date(2026, 10, 30))
    assert allocate([done, pending], 1) == [Block(done, 0), Block(pending, 1)]


def test_fractional_allocations_respect_budget_and_effort():
    tasks = [Task(str(i), 3, 0.1, date(2026, 10, 30)) for i in range(10)]
    blocks = allocate(tasks, 0.25)
    assert len(blocks) == 3
    assert [block.hours for block in blocks] == pytest.approx([0.1, 0.1, 0.05])
    assert sum(block.hours for block in blocks) == pytest.approx(0.25)
    assert all(0 <= block.hours <= block.task.effort_h for block in blocks)


def test_calls_do_not_share_results_or_consume_task_effort():
    task = Task("Study", 3, 2, date(2026, 10, 30))
    first = allocate([task], 1)
    second = allocate([task], 1)
    assert first == second == [Block(task, 1)]
    assert first is not second and first[0] is not second[0]
    assert task.effort_h == 2
