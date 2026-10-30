"""W3-1: Human-friendly date parsing."""

from __future__ import annotations

import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}
_IN_DAYS_PATTERN = re.compile(r"^in\s+(\d+)\s+days?$")


def parse_due(text: str, today: date) -> date:
    """Parse a human-friendly due date string relative to *today*.

    Supported formats:
    - ISO format date: ``"YYYY-MM-DD"``
    - ``"tomorrow"``: exactly 1 day after today
    - ``"in N days"`` / ``"in N day"``: N days after today
    - Weekday name (e.g. ``"Fri"``, ``"Friday"``): the next occurrence strictly
      after today (if today is Tuesday, ``"Tue"`` means 7 days later).

    Parameters
    ----------
    text : str
        The date string to parse.
    today : date
        Reference date for relative date resolution.

    Returns
    -------
    date
        The resolved calendar date.

    Raises
    ------
    ValueError
        If *text* cannot be parsed as a supported format.
    """
    clean = text.strip().lower()

    if clean == "tomorrow":
        return today + timedelta(days=1)

    if match := _IN_DAYS_PATTERN.match(clean):
        days = int(match.group(1))
        return today + timedelta(days=days)

    if clean in _WEEKDAYS:
        target_wd = _WEEKDAYS[clean]
        days_ahead = (target_wd - today.weekday()) % 7 or 7
        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(clean)
    except ValueError:
        raise ValueError(f"Cannot parse due date from {text!r}") from None
