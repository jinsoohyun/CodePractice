#Exercise 1065

#1~110 hansu = 99
def HansuCheck(n):
    tmp = 0
    if int(str(n)[1])-int(str(n)[0]) == int(str(n)[2])-int(str(n)[1]):
        return 1
    else:
        return 0

def isHansu(n):
    cnt = 0
    for i in range(111,n+1):
        if HansuCheck(i) == 1:
            cnt += 1
        else:
            pass
    return cnt

num = raw_input()
result = 0

if len(num) == 1:
    result = int(num)
    print result

elif len(num) == 2:
    result = int(num)
    print result

#input 1000
else:
    default = 99
    if int(num) <= 110:
        print 99
    else:
        print isHansu(int(num))+default

