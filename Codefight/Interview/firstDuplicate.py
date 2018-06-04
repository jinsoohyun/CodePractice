def firstDuplicate(a):
    dic, dupleIndex = {}, 0

    for i in range(len(a)):
        if a[i] in dic:
            dic[a[i]] += 1

        else:
            dic[a[i]] = 1

        if(dic[a[i]] == 2):
            return a[i]

    if not dupleIndex:
        return -1



'''
    lenList = len(a)
    lenSet = len(set(a))

    #check non Duplication
    if lenList == lenSet:
        return -1

    #check duplication
    else:
        return a[[idx for idx, item in enumerate(a) if item in a[:idx]][0]]
'''


'''
    try:
        return a[[idx for idx, item in enumerate(a) if item in a[:idx]][0]]
    except:
        return -1
'''

a = [2, 3, 3]
a = [2,2]



a = [2, 1, 3, 5, 3, 2]
a = [10, 6, 8, 4, 9, 1, 7, 2, 5, 3]
a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
print firstDuplicate(a)


