"""Tests for shared/study_planner/render.py (T-W2, THA Anh)."""

import sys
from datetime import date
from pathlib import Path

# Ensure python-bootcamp/ is on sys.path (mirrors conftest.py behaviour)
_BOOTCAMP = Path(__file__).resolve().parents[2]
if str(_BOOTCAMP) not in sys.path:
    sys.path.insert(0, str(_BOOTCAMP))

from shared.contract import Block, Task  # noqa: E402
from shared.study_planner.render import render  # noqa: E402


def _task(title: str, importance: int = 3, effort_h: float = 1.0) -> Task:
    return Task(title=title, importance=importance, effort_h=effort_h, deadline=date(2026, 11, 1))


def _block(title: str, hours: float) -> Block:
    return Block(task=_task(title), hours=hours)


# --- Empty input ---


def test_render_empty_returns_nothing_planned():
    assert render([]) == "Nothing planned."


# --- Single block ---


def test_render_single_block_header():
    result = render([_block("Assignment", 1.5)])
    assert result.startswith("Tonight (1.5 h):")


def test_render_single_block_line():
    result = render([_block("Assignment", 1.5)])
    assert "1. Assignment" in result
    assert "1.5 h" in result
    assert "." in result  # dot separator present


# --- Multiple blocks ---


def test_render_two_blocks_total():
    blocks = [_block("Assignment", 1.5), _block("DS exam", 0.5)]
    result = render(blocks)
    assert "Tonight (2.0 h):" in result


def test_render_two_blocks_numbering():
    blocks = [_block("Assignment", 1.5), _block("DS exam", 0.5)]
    lines = render(blocks).splitlines()
    assert "1." in lines[1]
    assert "2." in lines[2]


def test_render_two_blocks_order():
    """Tasks appear in the same order as the input list."""
    blocks = [_block("First", 1.0), _block("Second", 2.0)]
    lines = render(blocks).splitlines()
    assert "First" in lines[1]
    assert "Second" in lines[2]


# --- Totals ---


def test_render_total_is_sum_of_block_hours():
    blocks = [_block("A", 1.0), _block("B", 2.5), _block("C", 0.5)]
    assert "Tonight (4.0 h):" in render(blocks)


# --- Edge: zero-hour block ---


def test_render_zero_hour_block():
    """A block with 0 h is unusual but must not crash."""
    result = render([_block("Empty task", 0.0)])
    assert "Tonight (0.0 h):" in result
    assert "0.0 h" in result
