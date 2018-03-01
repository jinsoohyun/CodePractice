#Exercise 15552

import sys
count = sys.stdin.readline().rstrip()
for i in range(int(count)):
    strList = sys.stdin.readline().rstrip().split(' ')
    numList = map(int, strList)
    print sum(numList)
