def sortByHeight(a):
    indexList = []
    resultList = []

    for i in range(len(a)):
        if a[i] == -1:
            indexList.append(i)

    for i in range(len(indexList)):
        a.remove(-1)

    a.sort()
    arr = 0
    for i in range(len(a)+len(indexList)):
        if i in indexList:
            resultList.append(-1)
        else:
            resultList.append(a[arr])
            arr += 1

    return resultList

