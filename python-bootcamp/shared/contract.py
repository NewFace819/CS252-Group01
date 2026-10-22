"""Shared data contract for the study planner (T-W2, Section 18.6).

Every module in study_planner/ imports Task and Block from here, so a change to this
file needs approval from the whole team. Each module PR is reviewed against the
behaviour below. Module tests build Task and Block objects directly instead of
calling another member's module.

parse_csv(path) -> list[Task]                    parse.py (Đỗ Huy)
    Reads a CSV with the header title,importance,effort_h,deadline, deadline as
    YYYY-MM-DD. A bad row, including importance outside 1-5, raises
    ValueError("line N: ...") with the header counted as line 1.

prioritise(tasks, today) -> list[Task]           prioritise.py (Đức Huy)
    Returns a new list, highest importance / max(days_left, 1) first, where
    days_left = (deadline - today).days, so an overdue task counts as 1 day left.
    Ties go to the earlier deadline. The input list is not changed.

allocate(tasks, hours) -> list[Block]            allocate.py (Thông)
    Greedy, in the order given: each task gets min(effort_h, hours left) until no
    hours are left. hours <= 0 returns []. Tasks are not reordered.

render(blocks) -> str                            render.py (THA Anh)
    A readable plan in the W3-3 format, with the total of the blocks' hours:

        Tonight (2.0 h):
          1. Assignment ...... 1.5 h
          2. DS exam ......... 0.5 h

    An empty list returns "Nothing planned."
"""
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int      # 1-5
    effort_h: float
    deadline: date


@dataclass
class Block:
    task: Task
    hours: float
