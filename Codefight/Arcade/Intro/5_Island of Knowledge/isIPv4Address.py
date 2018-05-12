def isIPv4Address(inputString):
    host_bytes = inputString.split('.')
    if (len(host_bytes)>4):
        return False
    else:
        try:
            l = [int(i) for i in host_bytes if i != '' ]
            valid = [b for b in l if b >= 0 and b<=255]
            if len(valid) > 3:
                return True
            else:
                return False
        except:
            return False
