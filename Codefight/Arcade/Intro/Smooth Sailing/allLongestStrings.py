def allLongestStrings(inputArray):
    result = []
    maxLength = 0
    for i in inputArray:
        if maxLength < len(i):
            maxLength = len(i)
        
    for arr in inputArray:
        if (len(arr) == maxLength):
            result.append(arr)
    return result

