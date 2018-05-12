def boxBlur(image):
    defaultBox = 3
    width, height = len(image), len(image[0])
    result = []
    for w in range(width-2):
        tmp = []
        for h in range(height-2):
            #print w,h
            try:
                tmp.append((image[w][h]+image[w][h+1]+image[w][h+2]+image[w+1][h]+image[w+1][h+1]+image[w+1][h+2]+image[w+2][h]+image[w+2][h+1]+image[w+2][h+2])/9)
            except:
                continue

        #line by list
        if len(tmp) != 0:
            result.append(tmp)

    return result

image = [[7,4,0,1],
         [5,6,2,2],
         [6,10,7,8],
         [1,4,2,0]]

image = [[36,0,18,9],
         [27,54,9,0],
         [81,63,72,45]]

image = [[36,0,18,9,9,45,27],
 [27,0,54,9,0,63,90],
 [81,63,72,45,18,27,0],
 [0,0,9,81,27,18,45],
 [45,45,27,27,90,81,72],
 [45,18,9,0,9,18,45],
 [27,81,36,63,63,72,81]]


boxBlur(image)
