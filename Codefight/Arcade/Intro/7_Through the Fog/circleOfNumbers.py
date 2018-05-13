def circleOfNumbers(n, firstNumber):
    if firstNumber+(n/2) > n-1:
        return firstNumber-(n/2)
    return firstNumber+(n/2)

n = 6
firstNumber = 3
circleOfNumbers(n, firstNumber)
