# Exercise 10867
"""
10
1 4 2 3 1 4 2 3 1 2
"""
count = input()
num_list = raw_input().split(' ')
num_list = map(int, num_list)
num_list = list(set(num_list))
num_list.sort()

for i in num_list:
    print i,
