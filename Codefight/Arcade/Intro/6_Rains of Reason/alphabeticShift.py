def alphabeticShift(inputString):
    inputString = list(inputString)
    for i in range(len(inputString)):
        if (ord(inputString[i]) == 122): inputString[i] = 'a'
        else:
            inputString[i] = chr(ord(inputString[i])+1)

    return ''.join(inputString)
