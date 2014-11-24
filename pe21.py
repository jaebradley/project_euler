__author__ = 'jaebradley'

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def sum_div(x):
    div_sum = 0
    for div in range(1,x):
        if x%div == 0:
            div_sum += div
    return div_sum

import math
amicable_sum=0
for a in range(2,10001):
    sum_a = sum_div(a)
    b = sum_a
    sum_b = sum_div(sum_div(a))
    if sum_b == a & a != b:
        print a,b
        amicable_sum += (a+b)/2
print amicable_sum
