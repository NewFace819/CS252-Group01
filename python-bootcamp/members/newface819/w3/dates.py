from datetime import date, timedelta

WEEKDAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def parse_due(text: str, today: date) -> date:
    """
    Turn a due-date phrase into a date.

    Accepts "YYYY-MM-DD", "today", "tomorrow", "in N days" and weekday names
    such as "Fri" or "friday" (the next occurrence, never today).
    Raise ValueError for any other text.
    """
    s = text.strip().lower()
    if s == "today":
        return today
    if s == "tomorrow":
        return today + timedelta(days=1)
    words = s.split()
    if len(words) == 3 and words[0] == "in" and words[1].isdigit() and words[2] in ("day", "days"):
        return today + timedelta(days=int(words[1]))
    if s[:3] in WEEKDAYS and s in (s[:3], s[:3] + "day", "monday", "tuesday", "wednesday",
                                   "thursday", "friday", "saturday", "sunday"):
        ahead = (WEEKDAYS.index(s[:3]) - today.weekday()) % 7 or 7
        return today + timedelta(days=ahead)
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise ValueError(f"cannot understand due date: {text!r}") from None
