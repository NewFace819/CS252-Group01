def can_register_thesis(credits: int, gpa: float) -> bool:
    return (credits >= 120) and (gpa >= 2.0)

def missing(credits, gpa) -> list[str]:
    if can_register_thesis(credits, gpa):
        return []
    result = []
    if credits < 120:
        result.append(f"need {120 - credits} more credit{'s' if credits < 119 else ''}")
    if gpa < 2.0:
        result.append(f"need {round(2.0 - gpa, 2)} more GPA points")    
    return result
