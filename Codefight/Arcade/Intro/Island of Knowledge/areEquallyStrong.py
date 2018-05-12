def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft+yourRight == friendsLeft+friendsRight:
        #Case1 #yourLeft small, friendsLeft small
        if (yourLeft == friendsLeft or yourRight == friendsRight):
            return True

        elif (yourRight == friendsLeft or yourLeft == friendsRight):
            return True
        else:
            return False
    else:
        return False

