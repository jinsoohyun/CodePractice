# -*- coding: utf-8 -*-
#Exercise 10828
n = input()
stack = []

def cmdGenerator(cmd):
    cmd = cmd.strip()
    if 'push' in cmd:
        cmd, n = cmd.split(' ')
        stack.append(n)

    elif 'pop' in cmd:
        if len(stack) == 0:
            print -1
        else:
            print stack.pop()

    elif 'size' in cmd:
        print len(stack)

    elif 'empty' in cmd:
        if len(stack) > 0: print 0
        else: print 1

    elif 'top' in cmd:
        if len(stack) == 0: print -1
        else:
            print stack[-1]

for i in range(n):
    command = raw_input()
    cmdGenerator(command)
