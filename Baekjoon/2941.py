#Exercsie 2941

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=','a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#nljj
# n, l, j, j -> 4
# n, lj, j -> 3
# 그냥 replace하는 경우, n l j j 에서 lj 가 사라지고, nj 가 되어버려, nj 가 카운트 되어 버린다.
word = raw_input('')
sum = 0
for i in croatia:
    if i in word:
        #print "[=]",i
        if word.count >= 1:
            #print i
            sum += word.count(i)
        word = word.replace(i,' ')
print sum
