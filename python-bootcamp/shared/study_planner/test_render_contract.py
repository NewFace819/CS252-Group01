"""
T-W2: render() checked against shared/contract.py (Hải, paired with THA Anh on render.py).
"""
from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render

DEADLINE = date(2026, 10, 30)


def block(title: str, hours: float) -> Block:
    return Block(Task(title, 3, hours, DEADLINE), hours)


def test_w3_3_example_exact_output():
    got = render([block("Assignment", 1.5), block("DS exam", 0.5)])
    assert got == (
        "Tonight (2.0 h):\n"
        "  1. Assignment ................... 1.5 h\n"
        "  2. DS exam ...................... 0.5 h"
    )


def test_no_blocks():
    assert render([]) == "Nothing planned."


def test_keeps_input_order_and_numbers_from_one():
    lines = render([block("C", 1), block("A", 1), block("B", 1)]).splitlines()
    assert [line.split()[:2] for line in lines[1:]] == [["1.", "C"], ["2.", "A"], ["3.", "B"]]


def test_hours_column_is_aligned():
    lines = render([block("A", 1), block("Medium title", 2), block("DS exam", 0.5)]).splitlines()
    # Every task line ends with "H.H h", so equal lengths mean the hours line up.
    assert len({len(line) for line in lines[1:]}) == 1


def test_header_is_the_sum_of_block_hours():
    assert render([block("A", 1), block("B", 2.5), block("C", 0.5)]).startswith("Tonight (4.0 h):")


def test_header_matches_the_lines_with_quarter_hours():
    lines = render([block("Assignment", 1.5), block("DS exam", 0.75)]).splitlines()
    shown = [float(line.split()[-2]) for line in lines[1:]]
    assert lines[0] == f"Tonight ({sum(shown):.1f} h):"
