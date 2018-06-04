def bishopAndPawn(bishop, pawn):
    dic = {
        'a':0, 'b':1, 'c':2, 'd':3,
        'e':4, 'f':5, 'g':6, 'h':7
    }
    #print bishop, pawn



    dot1 = [dic[bishop[0]], int(bishop[1])-1]
    dot2 = [dic[pawn[0]], int(pawn[1])-1]
    #print "[!]",dot1, dot2

    bishopCanMove = []

    #right top check
    while (dot1[0] < 7):
        dot1 = [dot1[0]+1, dot1[1]+1]
        if dot1 == dot2:
            return True


    #left top check
    dot1 = [dic[bishop[0]], int(bishop[1])-1]
    while (dot1[0] > 0):
        dot1 = [dot1[0]-1, dot1[1]+1]
        if dot1 == dot2:
            return True

    #right down check
    dot1 = [dic[bishop[0]], int(bishop[1])-1]
    while (dot1[0] < 7):
        dot1 = [dot1[0]+1, dot1[1]-1]
        if dot1 == dot2:
            return True



    #left down check
    dot1 = [dic[bishop[0]], int(bishop[1])-1]
    while (dot1[0] > 0):
        dot1 = [dot1[0]-1, dot1[1]-1]
        print dot1
        if dot1 == dot2:
            return True

    return False



bishop = "e7"
pawn = "d6"
print bishopAndPawn(bishop, pawn)
