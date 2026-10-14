"""Count words while ignoring the punctuation listed in the W1 exercise."""


def word_count(text: str) -> dict[str, int]:
    """Lowercase text, remove . , ! ? ; : and count whitespace-separated words."""
    words = text.lower().translate(str.maketrans("", "", ".,!?;:")).split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return up to k words, by descending count then alphabetical order."""
    if k <= 0:
        return []
    return sorted(word_count(text).items(), key=lambda item: (-item[1], item[0]))[:k]
