"""W3-2: Analyse chat log requests, latencies, and p95 percentiles."""

from __future__ import annotations

import math
from collections import Counter, defaultdict


def p95(latencies: list[int]) -> int:
    """Calculate the 95th percentile using the nearest-rank method.

    The nearest-rank method selects the smallest value in the sorted list
    such that at least 95% of the measurements are at or below it.

    Parameters
    ----------
    latencies : list[int]
        Non-empty list of latency measurements.

    Returns
    -------
    int
        The 95th percentile latency.
    """
    sorted_vals = sorted(latencies)
    index = math.ceil(0.95 * len(sorted_vals)) - 1
    return sorted_vals[max(0, index)]


def analyse(pairs: list[tuple[str, int]]) -> dict:
    """Summarise a list of ``(route, latency_ms)`` log records.

    Parameters
    ----------
    pairs : list[tuple[str, int]]
        Pairs of endpoint route names and latency measurements in milliseconds.

    Returns
    -------
    dict
        A dictionary with the following keys:
        - ``"counts"``: mapping of route name to request count (Counter/dict).
        - ``"p95"``: mapping of route name to its 95th percentile latency (dict).
        - ``"slowest"``: the route with the highest p95 latency, or ``None`` if empty.
    """
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts = Counter(route for route, _ in pairs)
    grouped: defaultdict[str, list[int]] = defaultdict(list)
    for route, latency in pairs:
        grouped[route].append(latency)

    p95_by_route = {route: p95(lats) for route, lats in grouped.items()}
    slowest = max(p95_by_route, key=lambda k: p95_by_route[k])

    return {
        "counts": counts,
        "p95": p95_by_route,
        "slowest": slowest,
    }
