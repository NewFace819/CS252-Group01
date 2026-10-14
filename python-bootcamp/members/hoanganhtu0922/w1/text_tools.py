"""W1-2 Word counter."""


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text, case-insensitive, ignoring punctuation .,!?;:."""
    cleaned = text.lower().translate(str.maketrans("", "", ".,!?;:"))
    words = cleaned.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k frequent words sorted descending by count, then alphabetically ascending."""
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]
