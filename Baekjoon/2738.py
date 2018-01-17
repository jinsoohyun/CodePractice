#Exercise 2738

m = raw_input()
result = []
A = []
B = []

m = m.split(' ')
for n in range(2):
    for i in range(int(m[0])):
        #for j in range(int(m[1])):
        if (n==0):
            A.append(raw_input().split(' '))

        else:
            B.append(raw_input().split(' '))

for i in range(int(m[0])):
    for j in range(int(m[1])):
        print int(A[i][j]) + int(B[i][j]),
    print
