"""Parse explicit dates and relative deadlines against a supplied reference date."""

import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Accept YYYY-MM-DD, tomorrow, in N days, or Mon-Sun (strictly next).

    Surrounding whitespace and letter case are ignored. Unknown formats and
    dates outside Python's supported range raise ValueError.
    """
    value = text.strip().lower()
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return date.fromisoformat(value)
        if value == "tomorrow":
            return today + timedelta(days=1)
        relative = re.fullmatch(r"in (\d+) days", value)
        if relative:
            return today + timedelta(days=int(relative.group(1)))
        weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        if value in weekdays:
            offset = (weekdays.index(value) - today.weekday()) % 7 or 7
            return today + timedelta(days=offset)
    except (ValueError, OverflowError) as error:
        raise ValueError(f"Invalid deadline: {text!r}") from error
    raise ValueError(f"Unknown deadline: {text!r}")
