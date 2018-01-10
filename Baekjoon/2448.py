'''
default
  *
 * *
*****
  *     *
 * *   * *
***** *****
'''
import math

def drawStar(N):
    for i in range(len(star)):
        #append now triangle
        star.append(star[i] + star[i])

        #shift now triangle
        star[i] = space*N+star[i]+space*N

N = int(input())
star = ['  *   ',' * *  ', '***** ']
space = "   "

#shift space 3*2^(k-1)
k = int(math.log(N/3,2))

#make triangle
for i in range(k):
    drawStar(2**i)

#draw result
for i in star:
    print i
