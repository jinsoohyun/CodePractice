# -*- coding: utf-8 -*-
import Queue

"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
sequenceList = Queue.Queue([])

def confix(cmd):
    global sequenceList
    if ' ' in cmd:
        cmd, value = cmd.split(' ')

    if (cmd == 'push'):
        sequenceList.put(value)

    elif (cmd == 'pop'):
        if sequenceList.qsize() == 0:
            print -1
        else:
            print sequenceList.get()

    elif (cmd == 'size'):
        print sequenceList.qsize()

    elif (cmd == 'empty'):
        if sequenceList.qsize() == 0:
            print 1
        else:
            print 0

    elif (cmd == 'front'):
        if sequenceList.qsize() == 0:
            print -1
        else:
            print sequenceList.queue[0]

    elif (cmd == 'back'):
        if sequenceList.qsize() == 0:
            print -1
        else:
            print sequenceList.queue[-1]

sequenceCnt = input()
for i in range(sequenceCnt):
    confix(raw_input())
