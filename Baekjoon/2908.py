#Exercise 2908

numList = raw_input('').split(' ')

if int(numList[0][::-1]) > int(numList[1][::-1]):
    print int(numList[0][::-1])

else:
    print int(numList[1][::-1])
