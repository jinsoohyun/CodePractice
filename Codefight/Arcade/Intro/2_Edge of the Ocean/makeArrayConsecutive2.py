def makeArrayConsecutive2(statues):

    statues.sort()
    count = 0
    
    for i in range(statues[0],statues[-1]):
        if i not in statues:
            count += 1
    return count
            
