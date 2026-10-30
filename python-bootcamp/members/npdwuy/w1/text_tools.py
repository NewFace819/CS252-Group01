"""W1-2: word counts and the most frequent words of a text."""


def word_count(text: str) -> dict[str, int]:
    """Count each word, ignoring case and the punctuation .,!?;:"""
    sText = "".join(filter(lambda c: c not in ".,!?;:", text))
    result: dict[str, int] = {}
    for word in sText.split():
        word = word.lower()
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """The k most frequent (word, count) pairs, ties broken alphabetically; [] if k <= 0."""
    if k <= 0:
        return []
    result = list(word_count(text).items())
    result.sort(key=lambda e: (-e[1], e[0]))
    return result[:k]