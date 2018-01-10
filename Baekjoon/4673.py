#Exercise : 4673
bList = []
def isselfNumber(n):
    result = 0
    tmp = 0
    for i in str(n): tmp += int(i)

    result = tmp + n
    bList.append(result)

    if result > 10000: return 0
    isselfNumber(result)

for i in range(1,10001):
    isselfNumber(i)

aList = [int(i) for i in range(1,10001)]
notSelfNum = list(set(aList) - set(bList))
notSelfNum.sort()
for i in notSelfNum:
    print i
