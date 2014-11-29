'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

#find all abundant numbers <= 28123, find their sums, get the greatest sum, sum all the digits from 1 to greatest sum, subtract sum of abundant numbers

global greatest
global abundant_nums

def sum_div(x):
    div_sum = 0
    for div in range(1,x):
        if x%div == 0:
            div_sum += div
    return div_sum

def abundant(num):
    if sum_div(num) > num:
        return num

def abundant_list(x):
    abundant_nums=[]
    abundant_nums_sums=[]
    for i in range(1,x+1):
        if abundant(i) != None:
            abundant_nums.append(abundant(i))
    for p in abundant_nums:
        for q in abundant_nums:
            abundant_nums_sums.append(p+q)
    print abundant_nums_sums

def abundant_sum(n):
    sum_num = 0
    abundant_nums=[]
    abundant_nums_sums=[]
    numbers=[]
    for i in range(1,n+1):
        if abundant(i) != None:
            abundant_nums.append(abundant(i))
    for p in abundant_nums:
        for q in abundant_nums:
            abundant_nums_sums.append(p+q)
    for i in range(1,n+1):
        if i not in abundant_nums_sums:
            numbers.append(i)
    return sum(numbers)

print abundant_sum(28123)
