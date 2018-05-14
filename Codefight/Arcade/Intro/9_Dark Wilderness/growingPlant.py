def growingPlant(upSpeed, downSpeed, desiredHeight):
    cnt = 1
    totalPlant = 0
    #growSpeed = upSpeed - downSpeed
    while totalPlant < desiredHeight:
        totalPlant += upSpeed
        if totalPlant >= desiredHeight:
            return cnt
        totalPlant -= downSpeed
        cnt += 1
    return cnt


upSpeed = 10
downSpeed = 9
desiredHeight = 4
print growingPlant(upSpeed, downSpeed, desiredHeight)
