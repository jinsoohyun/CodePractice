# -*- coding: utf-8 -*-
#Exercise 9012
'''
() 문자열이 존재하는지 여부 확인을 통해 해결.
'''
sequenceNum = input()
for i in range(sequenceNum):
    result = ""
    PS = raw_input()

    for k in range(25):
        PS = PS.replace("()","")
        if (len(PS) == 0):
            result = "YES"
            break
        else:
            result = "NO"
    print result
