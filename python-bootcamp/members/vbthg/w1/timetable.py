"""Group courses by day, sorting each day's course list."""


def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Preserve day insertion order and retain repeated course entries."""
    grouped: dict[str, list[str]] = {}
    for course, day in pairs:
        grouped.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in grouped.items()}
