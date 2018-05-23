def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        if weight1 <= maxW and value1 > value2 :
            return value1
        elif weight2 <= maxW and value2 > value1:
            return value2
        elif maxW >= weight2:
            return value2
        elif maxW >= weight1:
            return value1
    return 0

value1= 10
weight1= 2
value2= 11
weight2= 3
maxW= 1


value1= 15
weight1= 2
value2= 20
weight2= 3
maxW= 2

print knapsackLight(value1, weight1, value2, weight2, maxW)

