import re
from datetime import date, timedelta

DAY_NAMES = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# "fri" and "friday" both map to 4, the same number date.weekday() gives a Friday.
WEEKDAYS = {name[:3]: i for i, name in enumerate(DAY_NAMES)} | {name: i for i, name in enumerate(DAY_NAMES)}
IN_N_DAYS = re.compile(r"in (\d+) days?")


def parse_due(text: str, today: date) -> date:
    """Turn a due date written by a person into a date.

    Accepts "2026-10-30", "tomorrow", "in 3 days" and weekday names such as "Fri" or
    "friday" (the next one after today, so "Tue" on a Tuesday means one week later).
    Raises ValueError for anything else.
    """
    s = text.strip().lower()
    if s == "tomorrow":
        return today + timedelta(days=1)
    if m := IN_N_DAYS.fullmatch(s):
        return today + timedelta(days=int(m.group(1)))
    if s in WEEKDAYS:
        ahead = (WEEKDAYS[s] - today.weekday()) % 7 or 7
        return today + timedelta(days=ahead)
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise ValueError(f"cannot read due date {text!r}") from None
