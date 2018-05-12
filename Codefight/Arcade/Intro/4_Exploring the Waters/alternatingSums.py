def alternatingSums(a):
    t1,t2 = (0,0)
    for idx in range(len(a)):
        if idx%2==0:
            t1 += a[idx]
        else:
            t2 += a[idx]
    
    return [t1,t2]

