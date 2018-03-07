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

def chkPair(tmp):
    tmp = tmp.replace('()','2')
    tmp = tmp.replace('[]','3')
    return tmp

#([)]
PS = raw_input()

dic = {'()':2, '[]':3}
result = []
tmp = 0
stackList = []
pop = 0
#stackList = list(PS[::-1])


if (isVPS(PS)):
    #([([]())])
    #([([3
    #([([3 )])
    # (()()(()))
    # (2 2 4
    for i in PS:
        tmp = 0
        #print "[!]",stackList, i
        if (i == '[' or i == '('):
            stackList.append(i)

        else:
            # 맨 위가. 숫자인 경우
            '''
            if str(stackList[-1]).isdigit():
                tmp += stackList.pop()

                #stackList.append(tmp)
            '''

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
                print "[=]"
                if (tmp == 0):
                    stackList.append(3)
                else:
                    stackList.append(tmp*3)

                    #tmp *= 2
                    #stackList.pop()
                    #stackList.append(tmp)

    print sum(stackList)
'''
if (isVPS(PS)):
    for i in PS:
        tmp += i
        #print "[+]", tmp
        if(len(tmp) > 1):
            if(dic.has_key(tmp[-2:])):
                if "()" in tmp:
                    tmp = tmp.replace("()","2")
                elif "[]" in tmp:
                    tmp = tmp.replace("[]","3")

                print "[+]", tmp
                if (tmp[-1] == ']' or tmp[-1] == ')'):
                    if tmp[-1] == ']':
                        result *= 3
                        tmp = tmp[:-3]

                    elif tmp[-1] == ')':
                        result *= 2
                        tmp = tmp[:-3]


                if tmp[-1].isdigit():
                    result += int(tmp[-1])
                    tmp = tmp[:-1]
                #print "[+]",tmp
        print result
'''

'''
tmp = PS
if (isVPS(tmp)):
    while(1):
        if ("(" not in tmp or "[" not in tmp):
            break

        else:
            tmp = chkPair(tmp)

'''
