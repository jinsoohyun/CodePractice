import string
import collections

l = string.lowercase
word = raw_input()
tmp_dic = dict(collections.Counter(l))

for key, value in tmp_dic.iteritems(): tmp_dic[key] -= 1

for key, value in dict(collections.Counter(word)).iteritems():
    tmp_dic[key] += value


#print "[+]",sorted(tmp_dic)
#print ' '.join(map(str,tmp_dic.values()))
for i in l:
    print tmp_dic[i],

