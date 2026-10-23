"""Allocate study time using the input order agreed in shared.contract."""

from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Greedily allocate the budget without reordering or modifying tasks.

    Each block keeps the original Task object. The last task may receive only
    part of its effort. A nonpositive budget produces no blocks.
    """
    blocks = []
    remaining = hours
    for task in tasks:
        if remaining <= 0:
            break
        allotted = min(task.effort_h, remaining)
        blocks.append(Block(task, allotted))
        remaining -= allotted
    return blocks
