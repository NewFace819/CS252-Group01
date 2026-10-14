PUNCTUATION = ".,!?;:"


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in text, ignoring case and specific punctuation."""
    cleaned = text.lower().translate(str.maketrans("", "", PUNCTUATION))
    words = cleaned.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k most frequent words sorted by count descending, then alphabetically."""
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]
