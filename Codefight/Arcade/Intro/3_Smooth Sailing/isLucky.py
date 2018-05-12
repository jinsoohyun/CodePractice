def isLucky(n):
    n = str(n)
    modNum = len(n)/2
    if sum(map(int,n[:modNum])) == sum(map(int, n[modNum:])):
        return True

    else:
        return False

