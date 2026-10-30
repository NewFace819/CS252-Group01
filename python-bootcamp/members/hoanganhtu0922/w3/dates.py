"""W3-1 Parse human-friendly due dates."""

from __future__ import annotations

import re
from datetime import date, timedelta

_NAMES = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
_FULL = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
_WEEKDAYS = {name: i for i, name in enumerate(_NAMES)} | {name: i for i, name in enumerate(_FULL)}
_IN_DAYS = re.compile(r"in (\d+) days?")


def parse_due(text: str, today: date) -> date:
    """Convert text such as "2026-10-30", "tomorrow", "in 3 days" or "Fri" to a date.

    A weekday name means its next occurrence, strictly after ``today``.
    Raises ValueError for any other text.
    """
    cleaned = text.strip().lower()

    if cleaned == "tomorrow":
        return today + timedelta(days=1)

    match = _IN_DAYS.fullmatch(cleaned)
    if match:
        return today + timedelta(days=int(match.group(1)))

    if cleaned in _WEEKDAYS:
        ahead = (_WEEKDAYS[cleaned] - today.weekday() - 1) % 7 + 1
        return today + timedelta(days=ahead)

    try:
        return date.fromisoformat(cleaned)
    except ValueError:
        raise ValueError(f"cannot parse due date: {text!r}") from None
