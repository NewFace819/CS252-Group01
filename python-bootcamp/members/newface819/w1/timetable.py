def by_day(pairs):
    """
    Group the course codes in (course, day) pairs by day.
    The course codes of each day are sorted.
    """
    d = {}
    for course, day in pairs:
        d.setdefault(day, []).append(course)
    for day in d:
        d[day].sort()
    return d
