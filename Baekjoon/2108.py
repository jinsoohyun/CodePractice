import sys
import collections

#python3
count = int(input())
txt = [0 for _ in range(count)]

for i in range(count):
    txt[i] = int(sys.stdin.readline())

#frequency check routine
txt.sort()
ctr = collections.Counter(txt)

#max value
t = ctr.most_common(1)[0][1]

result = []
for key in ctr.keys():
    if ctr[key] == t:
        result.append(key)

result.sort()
if len(result) > 1:
    result.pop(0)

print("{:.0f}".format(sum(txt)/count))
print(txt[(count+1)//2-1])
print(result[0])
print(txt[-1] - txt[0])
