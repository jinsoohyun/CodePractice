'''
def areSimilar(A, B):
    if sorted(A) == sorted(B):
        return sum([x != y for x, y in zip(A, B)]) <= 2
        #return sum(x != y for x, y in zip(A, B)) <= 2
        #return sum(x != y for x, y in zip(A, B)) <= 2
    return False
'''

def areSimilar(A, B):
    sortA, sortB = sorted(A), sorted(B)
    #sortB = sorted(B)
    if sortA != sortB:
        return False
    else:
        diffCnt = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                diffCnt+=1
    return diffCnt<=2

a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]

print areSimilar(a,b)
