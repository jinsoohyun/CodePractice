def arrayMaximalAdjacentDifference(inputArray):
    maxNum = 0
    for i in range(len(inputArray)-1):
        if maxNum < abs(inputArray[i]-inputArray[i+1]):
            maxNum = abs(inputArray[i]-inputArray[i+1])
    return maxNum
