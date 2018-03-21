N = input()
for i in range(N):
    a,b = map(int, raw_input().split(' '))
    result = 1

    if( a%10==0 ):
        result = 10
    else:
        for k in range(1,b+1):
             result *= a
             result %= 10


    print result
