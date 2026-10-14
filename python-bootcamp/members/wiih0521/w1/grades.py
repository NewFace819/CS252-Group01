def summary(scores: list[float]) -> dict:
    """Compute summary statistics (min, max, mean, median) for a list of scores."""
    if not scores:
        raise ValueError("Scores list cannot be empty")

    n = len(scores)
    sorted_scores = sorted(scores)

    mean = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": mean,
        "median": round(median, 2),
    }
