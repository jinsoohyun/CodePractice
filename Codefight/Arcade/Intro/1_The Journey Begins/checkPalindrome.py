import collections

def palindromeRearranging(inputString):
    cnt = 0
    reInput = inputString[::-1]
    if (reInput == inputString):
        return True
    else:
        tmp = dict(collections.Counter(inputString))
        print tmp
        for k,v in tmp.items():
            if v%2 == 1:
                cnt += 1
        if cnt >= 2:
            return False
        else:
            return True

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
print palindromeRearranging(inputString)



