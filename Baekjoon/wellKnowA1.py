N, Q, U, V = map(int, raw_input().split(' '))
A_sequence = map(int, raw_input().split(' '))
Max = 0


def Query1(C, A, B):
    global N, Q, U, V, A_sequence, Max
    tmpSum = sum(A_sequence[A-1:B])
    #print '[!]',A-1, B, tmpSum
    #print "[-]",tmpSum

    #if (Max < U*tmpSum+V*(len(A_sequence)-1)):
    Max = U*tmpSum+V*(B-A)
    print Max

# KA = B
def Query2(C, A, B):
    global N, Q, U, V, A_sequence
    A_sequence[A-1] = B
    #print A_sequence


for i in range(int(Q)):
    C, A, B = map(int, raw_input().split(' '))
    if (C == 0):
        Query1(C, A, B)

    else:
        Query2(C, A, B)

