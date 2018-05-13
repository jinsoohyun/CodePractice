def chessBoardCellColor(cell1, cell2):
    dic = {
        'A':0, 'B':1, 'C':2, 'D':3,
        'E':4, 'F':5, 'G':6, 'H':7
    }

    dot1 = [dic[cell1[0]], int(cell1[1])-1]
    dot2 = [dic[cell2[0]], int(cell2[1])-1]
    print dot1, dot2
    if dot1[0]%2 == dot2[0]%2 and dot1[1]%2 == dot2[1]%2:
        return True
    elif dot1[0]%2 != dot2[0]%2 and dot1[1]%2 != dot2[1]%2:
        return True
    else:
        return False




cell1 = "A1"
cell2 = "H3"
print chessBoardCellColor(cell1, cell2)

