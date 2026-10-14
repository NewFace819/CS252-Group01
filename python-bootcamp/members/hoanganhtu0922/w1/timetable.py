"""W1-5 Group the timetable."""


def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day into a dictionary with sorted course lists."""
    result: dict[str, list[str]] = {}
    for course, day in pairs:
        result.setdefault(day, []).append(course)
    for day in result:
        result[day].sort()
    return result
