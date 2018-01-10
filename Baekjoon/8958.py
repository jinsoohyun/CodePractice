#Exercise 8958
correctList = []
count = input('')
for i in range(count):
    correctList.append(raw_input(''))
for i in correctList:
    cnt = 0
    score = 0
    for k in i:
        if k == 'O':
            cnt += 1
            score += cnt
        elif k == 'X':
            #score += cnt
            cnt = 0
    print score
