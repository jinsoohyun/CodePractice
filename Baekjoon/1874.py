# -*- coding: utf-8 -*-
#Exercise 1874

sequenceNum = input()

baselist = [i for i in range(sequenceNum,0,-1)]
listA = [input() for i in range(sequenceNum)]

listA = listA[::-1]
tmp = []
fg = 0
result = ""

tmp.append(baselist.pop())
result += "+"
cnt = sequenceNum-1

while(1):
    if ((len(baselist) < 1 and len(tmp) == 0)):
        break

    else:
        #아직 남아있는데 스택 비워진경우
        if ((len(baselist) > 0 and len(tmp) == 0)):
            tmp.append(baselist.pop())
            result += "+"

        #스택 맨위 항목이 수열 스택 항목과 다른경우
        if (tmp[-1] != listA[cnt]):
            if (len(baselist) == 0):
                result = "NO"
                #print "No"
                break

            tmp.append(baselist.pop())
            result += "+"

        elif (tmp[-1] == listA[cnt]):
            cnt = cnt-1
            tmp.pop()
            result += "-"

if ("NO" not in result):
    for i in result:
        print i

else:
    print result
