def restoreString(s, indices):
    res = [''] * len(s)
    for k, i in enumerate(indices):
        res[i] = s[k]
    return ''.join(res)


def restoreString2(s, indices):
    combo = []
    for i in range(len(s)):
        combo.append([indices[i], s[i]])

    sorted_combo = sorted(combo, key=lambda x: x[0])
    _, word = list(zip(*sorted_combo))
    return ''.join(word)


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
print(restoreString2(s, indices))
# print(restoreString(s, indices))
