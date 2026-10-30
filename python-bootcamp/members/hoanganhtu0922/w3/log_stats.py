"""W3-2 Request statistics per route."""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from typing import Any


def _p95(values: list[int | float]) -> int | float:
    """Return the 95th percentile (nearest-rank) of a non-empty list."""
    ordered = sorted(values)
    rank = math.ceil(0.95 * len(ordered))
    return ordered[rank - 1]


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Summarise (route, latency_ms) pairs.

    Returns {"counts": Counter of requests per route,
             "p95": p95 latency per route,
             "slowest": route with the highest p95, or None if no data}.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[int | float]] = defaultdict(list)
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95 = {route: _p95(values) for route, values in latencies.items()}
    slowest = max(p95, key=lambda r: p95[r]) if p95 else None
    return {"counts": counts, "p95": p95, "slowest": slowest}
