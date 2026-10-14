"""W1-1 Grade summary."""


def summary(scores: list[float]) -> dict[str, float]:
    """Calculate min, max, mean, and median of scores.

    Mean and median are rounded to 2 decimal places.
    Raises ValueError if scores is empty.
    """
    if not scores:
        raise ValueError("scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    min_score = sorted_scores[0]
    max_score = sorted_scores[-1]
    mean_score = round(sum(sorted_scores) / n, 2)

    if n % 2 == 1:
        median_score = sorted_scores[n // 2]
    else:
        median_score = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    median_score = round(median_score, 2)

    return {
        "min": min_score,
        "max": max_score,
        "mean": mean_score,
        "median": median_score,
    }
