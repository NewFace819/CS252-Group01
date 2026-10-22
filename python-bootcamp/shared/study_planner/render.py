"""T-W2 render.py — format a list of Blocks into a readable study plan.

Imported types come from shared/contract.py so every module in
study_planner/ uses the same Task and Block dataclasses.
"""

from __future__ import annotations

from shared.contract import Block

_LINE_WIDTH = 36  # total chars for "title ....... H.H h" part


def render(blocks: list[Block]) -> str:
    """Return a human-readable plan string.

    Format::

        Tonight (2.0 h):
          1. Assignment ...... 1.5 h
          2. DS exam ......... 0.5 h

    An empty list returns "Nothing planned."
    """
    if not blocks:
        return "Nothing planned."

    total = sum(b.hours for b in blocks)
    lines: list[str] = [f"Tonight ({total:.1f} h):"]

    for i, block in enumerate(blocks, start=1):
        title = block.task.title
        hours_str = f"{block.hours:.1f} h"
        # Fill the gap between title and hours with dots
        gap = _LINE_WIDTH - len(title) - len(hours_str)
        dots = "." * max(1, gap - 2)  # -2 for the spaces around the dots
        lines.append(f"  {i}. {title} {dots} {hours_str}")

    return "\n".join(lines)
