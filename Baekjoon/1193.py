#Exercise 1193
x = input('')
n = 1

#find line count
while n*(n+1)/2 < x:
    n += 1

#calculator
n -= 1
gap = x-n*(n+1)/2
if n%2 == 1:
    print str(gap)+"/"+str(n+2-gap)
elif n%2 == 0:
    print str(n+2-gap)+"/"+str(gap)
