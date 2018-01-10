#Exercise 10039
scoreList = []
for i in range(5): scoreList.append(input())
Sum = 0

for i in scoreList:
    if i<40:
        i = 40
        Sum += 40
    else:
        Sum += i
print Sum/5
