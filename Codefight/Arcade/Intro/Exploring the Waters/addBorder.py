def addBorder(picture):
    result = []
    init = len(picture)
    init_arr = len(picture[0])
    
    result.append('*'*(init_arr+2))
    for i in picture:
        result.append("*"+i+"*")
    result.append('*'*(init_arr+2))
    return result

