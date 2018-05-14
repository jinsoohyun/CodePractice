def extractEachKth(inputArray, k):
    result = []
    for i in range(len(inputArray)):
        if i%k != k-1:
            result.append(inputArray[i])
    return result


inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print extractEachKth(inputArray, k)
