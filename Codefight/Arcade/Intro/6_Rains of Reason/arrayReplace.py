def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for n,i in enumerate(inputArray):
        if (i == elemToReplace):
            inputArray[n] = substitutionElem
    return inputArray
