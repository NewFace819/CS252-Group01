"""W1-3 Thesis eligibility rules."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if credits >= 120 and gpa >= 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return list of human-readable reasons if not eligible to register thesis."""
    reasons: list[str] = []
    if credits < 120:
        needed = 120 - credits
        unit = "credit" if needed == 1 else "credits"
        reasons.append(f"need {needed} more {unit}")
    if gpa < 2.0:
        reasons.append("need a GPA of at least 2.0")
    return reasons
