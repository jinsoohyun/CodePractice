num = raw_input("")
num1, num2 = num.split(' ')

num_list = raw_input("").split(' ')
result = []
for i in num_list:
	if int(i) < int(num2):
		result.append(i)

print ' '.join(result)
