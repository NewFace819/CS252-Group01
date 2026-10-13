def can_register_thesis(credits, gpa):
    return credits >= 120 and gpa >= 2.0


def missing(credits, gpa) -> list[str]:
    if(can_register_thesis(credits, gpa)):
        return []
    ans = []
    if(credits < 120):
        ans.append("need {x} more credits".format(x=max(0, 120 - credits)))
    if(gpa < 2.0):
        ans.append("need {y} more GPA".format(y=max(0, 2.0 - gpa)))
    return ans