def digitDegree(n):
    cnt = 0
    sumNum = 0


    while(len(str(n))!=1):
        cnt += 1
        n = sum(map(int, str(n)))
        #print n

    return cnt

n = 99
digitDegree(n)
