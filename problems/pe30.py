__author__ = 'jaebradley'

num_list = []
num_sum = 0
for num in range(2,355000):
    sum = 0
    for i in str(num):
        sum += int(i)**5
    if sum == num:
        num_sum += num
        num_list.append(num)

print num_sum