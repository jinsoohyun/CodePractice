n = input()
cnt = 0
if n < 3 or n == 4 or n == 7:
    print -1
    quit()


while(n > 0):
    if n%5 ==0:
        n -= 5
        cnt +=1

    elif n%3 == 0:
        n -= 3
        cnt += 1

    elif n%5 !=0 and n%3 !=0:
        n -= 5
        cnt += 1
print cnt
