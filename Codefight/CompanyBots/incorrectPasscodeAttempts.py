def incorrectPasscodeAttempts(passcode, attempts):
    lockCnt = 0
    for i in attempts:
        if i != passcode:
            lockCnt += 1
            if lockCnt >= 10:
                return True
        else:
            lockCnt = 0
    return False



attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
passcode = "1111"
print incorrectPasscodeAttempts(passcode, attempts)
