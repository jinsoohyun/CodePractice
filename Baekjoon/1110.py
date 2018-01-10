number = raw_input('')

num = int(number)
total = 0
cnt = 0
while True:
    total = 0
    for i in str(number):
        total += int(i)
    cnt += 1
    number = int(str(number)[-1]+str(total)[-1])

    if int(number) == num:
        print cnt
        quit()
