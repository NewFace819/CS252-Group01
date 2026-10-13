def summary(score: list[float]) -> dict:
    if(len(score) == 0):
        raise ValueError
    score.sort()
    d = {}
    d["min"] = score[0]
    d["max"] = score[-1]
    d["mean"] = sum(score) / len(score)
    if(len(score) % 2 == 0):
        d["median"] = (score[len(score) // 2 - 1] + score[len(score) // 2]) / 2
    else:
        d["median"] = score[len(score) // 2]
    d["mean"] = round(d["mean"], 2)
    d["median"] = round(d["median"], 2)
    
    return d