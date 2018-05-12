def shapeArea(n):
    prevSum = 1
    for i in range(1,n+1):
        prevSum = prevSum + (i*2)+(i-2)*2
    return prevSum


