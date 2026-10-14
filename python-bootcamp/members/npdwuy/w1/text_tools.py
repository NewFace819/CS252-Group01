def word_count(text: str) -> dict[str, int]:
    sText = "".join(filter(lambda c: c not in ".,!?;:", text))
    result = {}
    for word in sText.split():
        word = word.lower()
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0: return []
    result = list(word_count(text).items())
    result.sort(key=lambda e: (-e[1], e[0]))
    return result[:k]