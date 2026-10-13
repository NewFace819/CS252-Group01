def word_count(text):
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



def top_k(text, k):
    d = word_count(text)
    ans = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    return ans[:k]
