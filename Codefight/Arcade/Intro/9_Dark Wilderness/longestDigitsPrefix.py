def longestDigitsPrefix(inputString):
    tmp = []
    tmpString = ""
    maxString = ''
    if not inputString[0].isdigit():
        return ''

    for i in inputString:
        if i.isdigit():
            tmpString += i
        else:
            if len(tmpString)>0:
                if len(maxString) < len(tmpString):
                    maxString = tmpString

                tmp.append(tmpString)
                tmpString = ''

    if len(tmpString)>0:
        if len(maxString) < len(tmpString):
            maxString = tmpString
        tmp.append(tmpString)

    return maxString


inputString = "  3) always check for whitespaces"
inputString = "the output is 42"
print longestDigitsPrefix(inputString)
