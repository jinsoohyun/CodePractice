import itertools

def compareString(s1,s2):
    cnt = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            cnt += 1
    return cnt == 1

def stringsRearrangement(inputArray):
    allCase = itertools.permutations(inputArray)

    for case in allCase:
        tmp = True
        for i in range(len(case)-1):
            if not compareString(case[i], case[i+1]):
                tmp = False
                break
        if tmp:
            return True
    return False







inputArray = ["ab",
 "bb",
 "aa"]


inputArray = ["aba",
 "bbb",
 "bab"]


inputArray = ["abc",
 "abx",
 "axx",
 "abx",
 "abc"]

inputArray = ["abc",
 "abx",
 "axx",
 "abc"]

print stringsRearrangement(inputArray)
