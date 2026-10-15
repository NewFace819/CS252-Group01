def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group (course, day) pairs into {day: sorted list of courses}."""
    result: dict[str, list[str]] = {}
    for course, day in pairs:
        result.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in result.items()}
