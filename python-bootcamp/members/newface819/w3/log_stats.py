from collections import Counter, defaultdict
from math import ceil


def p95(values: list[float]) -> float:
    """
    Return the 95th percentile of values (nearest-rank method).
    """
    ordered = sorted(values)
    return ordered[ceil(0.95 * len(ordered)) - 1]


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """
    Summarise (route, latency_ms) pairs.

    Return {"counts": requests per route, "p95": p95 latency per route,
    "slowest": the route with the highest p95}. An empty list raises ValueError.
    """
    if not pairs:
        raise ValueError("no requests to analyse")
    counts = Counter(route for route, _ in pairs)
    latencies: dict[str, list[float]] = defaultdict(list)
    for route, ms in pairs:
        latencies[route].append(ms)
    p95s = {route: p95(values) for route, values in latencies.items()}
    return {"counts": dict(counts), "p95": p95s, "slowest": max(p95s, key=p95s.__getitem__)}
