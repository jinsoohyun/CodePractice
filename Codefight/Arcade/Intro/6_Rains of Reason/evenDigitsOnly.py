def evenDigitsOnly(n):
    for i in str(n):
        if (int(i)%2 != 0):
            return False
    return True
