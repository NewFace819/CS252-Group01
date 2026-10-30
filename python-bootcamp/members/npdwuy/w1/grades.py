"""W1-1: summary statistics for a list of scores."""


def summary(scores: list[float]) -> dict[str, float]:
    """Return {"min", "max", "mean", "median"} of scores, mean and median rounded to 2 places.

    Raises ValueError for an empty list.
    """
    n = len(scores)
    if n == 0:
        raise ValueError("The scores list is empty.")
    s = sorted(scores)
    if n % 2 == 0:
        med = (s[n // 2 - 1] + s[n // 2]) / 2
    else:
        med = s[n // 2]
    result = {"min": s[0], 
              "max": s[-1], 
              "mean": round(sum(s) / n, 2),
              "median": round(med, 2)}
    return result