#Exercise 1181
count = input()
txt = []
for i in range(count):
    t = raw_input()
    txt.append((len(t), t))
txt = list(set(txt))
txt.sort()
for legth, word in txt:
    print word
'''
13 but i wont hesitate no more no more it cannot wait im yours
'''

