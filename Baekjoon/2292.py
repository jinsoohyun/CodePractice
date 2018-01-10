#Exercsie 2292

def isPathCheck(n):
    result = 1
    cnt = 1
    while result < n:
        result += (6*cnt)
        cnt += 1
    return cnt


print isPathCheck(input(''))
