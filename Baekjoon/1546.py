n = input("")
score = raw_input("").split(' ')

total = 0
new_score = []
score = map(int, score)
max_score = int(max(score))

for i in score: total += float(i)/float(max_score)*100.0

print '%.2f'%round(float(total)/float(n),2)
