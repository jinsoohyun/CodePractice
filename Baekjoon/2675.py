#Exercise 2675

count = input('')
strList = []

for i in range(count):
    strList.append(raw_input(""))

result = ""
for i in strList:
    result = ""
    cnt = i.split(' ')[0]
    word = i.split(' ')[1]
    for k in word:
        result += int(cnt)*k
    print result
