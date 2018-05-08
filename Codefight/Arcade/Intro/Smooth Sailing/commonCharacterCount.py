import collections
def commonCharacterCount(s1, s2):
    dicS1 = dict(collections.Counter(s1))
    dicS2 = dict(collections.Counter(s2))
    result = 0

    for i in dicS1:
        if i in dicS2:
            if dicS1[i] <= dicS2[i]:
                result += dicS1[i]
            else:
                result += dicS2[i]
    return result

