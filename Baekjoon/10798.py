'''
ABCDE
abcde
01234
FGHIJ
fghij
'''
l = []
Max = 0
result = ""
for i in range(5):
    l.append(raw_input())
    if Max < len(l[i]):
        Max = len(l[i])


for i in range(Max):
    for j in range(5):
        try:
            result += l[j][i]

        except:
            pass

print result
