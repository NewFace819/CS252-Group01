def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return a dict mapping each day to a sorted list of courses."""
    schedule: dict[str, list[str]] = {}
    for course, day in pairs:
        schedule.setdefault(day, []).append(course)

    for courses in schedule.values():
        courses.sort()

    return schedule
