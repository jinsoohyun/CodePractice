# -*- coding: utf-8 -*-
#Exercise 2504
'''
() 문자열이 존재하는지 여부 확인을 통해 해결.
'''

def isVPS(PS):
    if (PS.count("[") != PS.count("]") or PS.count("(") != PS.count(")")):
        print 0
        exit(0)

    for i in range(15):
        if ("[]" in PS or "()" in PS):
            PS = PS.replace("[]","")
            PS = PS.replace("()","")
            if (len(PS) == 0):
                return 1
    print 0
    exit(0)

PS = raw_input()

result = []
stackList = []

tmp = 0
pop = 0

if (isVPS(PS)):
    for i in PS:
        tmp = 0
        #print "[!]",stackList, i
        if (i == '[' or i == '('):
            stackList.append(i)

        else:
            # 맨 위가. 숫자인 경우
            pop = stackList.pop()
            while pop != '[' and pop != '(':
                tmp += int(pop)
                pop = stackList.pop()

            # 맨 위가 숫자가 아닌 경우
            if (i == ')'):
                if (tmp == 0):
                    stackList.append(2)
                else:
                    stackList.append(tmp*2)

            else:
                if (tmp == 0):
                    stackList.append(3)
                else:
                    stackList.append(tmp*3)

    print sum(stackList)
