def arrayChange(inputArray):
    cnt = 0
    for i in range(1,len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            sequence = (inputArray[i-1]-inputArray[i])+1
            inputArray[i] += sequence
            cnt += sequence
        #print inputArray[i]
    print cnt









inputArray = [1, 1, 1]
arrayChange(inputArray)
