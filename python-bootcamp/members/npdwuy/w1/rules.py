"""W1-3: thesis registration rule (at least 120 credits and GPA 2.0)."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """True if the student has at least 120 credits and a GPA of at least 2.0."""
    return (credits >= 120) and (gpa >= 2.0)


def missing(credits: int, gpa: float) -> list[str]:
    """List what the student still needs to register, or [] if they can register now."""
    if can_register_thesis(credits, gpa):
        return []
    result = []
    if credits < 120:
        result.append(f"need {120 - credits} more credit{'s' if credits < 119 else ''}")
    if gpa < 2.0:
        result.append(f"need {round(2.0 - gpa, 2)} more GPA points")    
    return result
