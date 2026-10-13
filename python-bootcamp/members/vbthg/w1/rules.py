"""Check the thesis eligibility thresholds specified in W1."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Require at least 120 credits and a GPA of at least 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Explain each unmet requirement, credits first and GPA second."""
    reasons = []
    if credits < 120:
        deficit = 120 - credits
        unit = "credit" if deficit == 1 else "credits"
        reasons.append(f"need {deficit} more {unit}")
    if gpa < 2.0:
        reasons.append("need a GPA of at least 2.0")
    return reasons
