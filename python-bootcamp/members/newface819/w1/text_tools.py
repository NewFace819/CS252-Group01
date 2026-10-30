def word_count(text: str) -> dict[str, int]:
    """
    Count how many times each word appears in text.
    Words are lower-cased and the punctuation .,!?;: is ignored.
    """
    text = text.lower()
    for c in ['.', ',', '!', '?', ';', ':']:
        text = text.replace(c, "")
    d = text.split()
    ans = {}
    for word in d:
        if word in ans:
            ans[word] += 1
        else:
            ans[word] = 1
    return ans



def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """
    Return the k most frequent words in text as (word, count) pairs.
    Words with the same count are sorted alphabetically.
    """
    d = word_count(text)
    ans = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    return ans[:k]
