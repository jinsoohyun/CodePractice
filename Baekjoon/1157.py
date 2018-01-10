#Exercise 1157
#Mississipi
import string

dic = {}

word = raw_input('').upper()
cntResult = []
for i in string.uppercase:
    dic.update({i:word.count(i)})

# if max value is only one
if len([key for key, val in dic.items() if val == max(dic.values())]) >= 2:
    print '?'
# else max value is more than one
else:
    result = ''.join([key for key, val in dic.items() if val == max(dic.values())])
    print result.upper()
