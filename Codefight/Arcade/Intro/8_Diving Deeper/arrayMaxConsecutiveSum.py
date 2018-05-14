'''not DP Code >> Fail. time limit
def arrayMaxConsecutiveSum(inputArray, k):
    maxSum = 0
    for i in range(len(inputArray)-(k-1)):
        #print i
        tmp = 0
        for j in range(k):
            #print inputArray[i+j],
            tmp +=  inputArray[i+j]
        if maxSum < tmp:
            maxSum = tmp
        #print
    return maxSum
'''
def arrayMaxConsecutiveSum(inputArray, k):
    initSum = sum(inputArray[0:k])
    maxSum = initSum

    for i in range(k,len(inputArray)):
        print inputArray[i-k], inputArray[i]
        initSum = initSum - inputArray[i-k] + inputArray[i]
        if initSum > maxSum:
            maxSum = initSum
    return maxSum



inputArray = [1, 3, 4, 2, 4, 2, 4]
k = 4
print arrayMaxConsecutiveSum(inputArray, k)
