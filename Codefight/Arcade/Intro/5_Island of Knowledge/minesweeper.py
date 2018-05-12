def minesweeper(matrix):
    defaultBox = 3
    height,width = len(matrix), len(matrix[0])
    result = []
    for i in range(height):
        tmp = []
        for j in range(width):
            tmp.append(0)
        result.append(tmp)

    for h in range(height):
        tmp = []
        for w in range(width):
            if (matrix[h][w] == True):
                for cnt in range(8):
                    flag = cnt%8
                    try:
                        if flag == 0:
                            if (h-1 < 0 or w-1 < 0): continue
                            result[h-1][w-1] += 1

                        elif flag == 1:
                            if (h-1 < 0): continue
                            result[h-1][w] += 1

                        elif flag == 2:
                            if (h-1 < 0): continue
                            result[h-1][w+1] += 1

                        elif flag == 3:
                            if (w-1 < 0): continue
                            result[h][w-1] += 1

                        elif flag == 4:
                            result[h][w+1] += 1

                        elif flag == 5:
                            if (w-1 < 0): continue
                            result[h+1][w-1] += 1

                        elif flag == 6:
                            result[h+1][w] += 1

                        elif flag == 7:
                            result[h+1][w+1] += 1
                    except: continue
    return result



matrix = [[False,False,False],
 [False,False,False]]

matrix = [[True,False,False],
 [False,True,False],
 [False,False,False]]

matrix = [[True,False,False,True],
        [False,False,True,False],
        [True,True,False,True]]




minesweeper(matrix)

