import math
from collections import Counter, defaultdict


def p95(latencies: list[int]) -> int:
    """95th percentile by the nearest-rank method: the smallest value that at least 95% of
    the requests are at or below, so it is always one of the measured latencies."""
    ordered = sorted(latencies)
    return ordered[math.ceil(0.95 * len(ordered)) - 1]


def analyse(pairs: list[tuple[str, int]]) -> dict:
    """Summarise a chat log given as (route, latency_ms) pairs.

    Returns {"counts": requests per route, "p95": p95 latency per route,
    "slowest": the route with the highest p95, or None for an empty log}.
    """
    counts = Counter(route for route, _ in pairs)
    by_route: defaultdict[str, list[int]] = defaultdict(list)
    for route, ms in pairs:
        by_route[route].append(ms)
    p95s = {route: p95(ms) for route, ms in by_route.items()}
    return {"counts": counts, "p95": p95s, "slowest": max(p95s, key=p95s.get, default=None)}
