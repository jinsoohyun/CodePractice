#Exercise 6064
import sys

def findYear(m,n,x,y):
    mul=m*n;
    result = -1
    if(x<=m and y<=n):
        for j in range(x,mul+1,m):
            if((j-1)%n+1==y):
                result=j;
                break;
        print result

count = sys.stdin.readline().rstrip()
for i in range(int(count)):
    strList = sys.stdin.readline().rstrip().split(' ')
    M,N,x,y = map(int,strList)
    findYear(M,N,x,y)
