def avoidObstacles(inputArray):
    inputArray.sort()
    jmp_list = []
    for i in range(2,inputArray[-1]):
        #print i,
        if i not in inputArray:
            jmp_list.append(i)

    print '[!] jmp list : ',jmp_list
    if len(jmp_list) == 0:
        return inputArray[-1]+1


    else:
        for i in jmp_list:
            tmp = i
            while tmp <= inputArray[-1]:
                if tmp in inputArray:
                    tmp = i
                    break
                else:
                    tmp += i
            if tmp != i:
                return i

        '''
        for i in range(len(jmp_list)-1):
            if (jmp_list[i+1]%jmp_list[i] == 0):
                return jmp_list[0]

        return jmp_list[len(jmp_list)/2]
        '''

inputArray = [2, 3]
#inputArray = [5, 3, 6, 7, 9]
#inputArray = [1, 4, 10, 6, 2]
#inputArray = [19, 32, 11, 23]
print avoidObstacles(inputArray)
