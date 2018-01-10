#Exercise 1316

def isGroupWord(word):
    lenWord = len(word)
    for i in range(1,lenWord):
        if word[i] != word[i-1]:
            if word[i-1] in word[i+1:]:
                return 0
    return 1

count = input('')
wordList = []
for i in range(count):
    wordList.append(raw_input(''))

sum = 0
for word in wordList:
    if isGroupWord(word) == True:
        sum += 1
print sum
