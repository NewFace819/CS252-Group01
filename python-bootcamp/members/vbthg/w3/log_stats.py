"""Summarise per-route latency using the nearest-rank 95th percentile."""

from collections import Counter, defaultdict
from math import ceil, isfinite
from typing import Iterable, TypedDict


class LogStats(TypedDict):
    """Counts, p95 latency per route, and the route with the highest p95."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: Iterable[tuple[str, float]]) -> LogStats:
    """Compute p95 as sorted_values[ceil(0.95 * n) - 1].

    Empty input has no slowest route. Equal p95 values use alphabetical route
    order, making the result independent of input order. Latencies must be
    finite and nonnegative.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)
    for route, latency_ms in pairs:
        if not isfinite(latency_ms) or latency_ms < 0:
            raise ValueError("latency_ms must be finite and nonnegative")
        counts[route] += 1
        latencies[route].append(latency_ms)
    p95 = {
        route: sorted(values)[ceil(0.95 * len(values)) - 1]
        for route, values in latencies.items()
    }
    slowest = min(p95, key=lambda route: (-p95[route], route)) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
