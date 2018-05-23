#replay!!
def find_largetst_length(windows, inputString, index):
    length_list = list(range(1, len(windows)+1))
    length_list.reverse()
    for length in length_list:
        if inputString[index:index+length] in windows:
            if index+length > len(inputString):
                return windows.index(inputString[index:index+length]), len(inputString)-index, inputString[index:index+length]

            else:
                return windows.index(inputString[index:index+length]),length, inputString[index:index+length]


def losslessDataCompression(inputString, width):
    windows = ""
    result = ""

    i = 0
    length = 0
    word_len = len(inputString)
    while i < word_len:
        char = inputString[i]
        if char not in windows:
            result += char
        else:
            windows_index, length, compressed_value = find_largetst_length(windows, inputString, i)
            start_index = inputString.find(compressed_value, i-len(windows))
            result += "("+ str(start_index) +","+str(length) +")"
            i += length-1
            length = 0

        if i < width:
            windows = inputString[:i+1]
        else:
            windows = inputString[i-width+1:i+1]
        if length == 0:
            i+=1
    return result
