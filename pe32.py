__author__ = 'jaebradley'

'''
Want to find all numbers for m * n = z where concat(m, n, z) uses all digits from 1-9 exactly once
Only 2 ways to get this: either m is a 1 digit number and n is a 4 digit number OR m is a 2 digit number and n is a 3 digit number
So iterate through all possible m and n and check if concat(m, n, z) is pandigital
'''

import math
import time

def is_pandigital(number):
    digit_list = getDigits(number)
    if (max(digit_list) != len(digit_list)) or (min(digit_list) != 1):
        return 0
    else:
        for i in range(1,len(digit_list) + 1):
            try:
                digit_list.remove(i)
            except ValueError:
                return 0
        if not digit_list:
            return 1
        else:
            return 0

def getDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return digit_list

def getProduct(start_range_m,end_range_m,start_range_n,end_range_n,pandigital_list):
    for m in range(start_range_m,end_range_m + 1):
        for n in range(start_range_n,end_range_n + 1):
            product = m * n
            number = int(str(m) + str(n) + str(product))
            if is_pandigital(number):
                pandigital_list.append(product)
    return pandigital_list

start_time = time.time()
pandigital_list = []

pandigital_list = getProduct(0,9,1000,9999,pandigital_list)
pandigital_list = getProduct(10,99,100,999,pandigital_list)
end_time = time.time()
unique_pandigitals = set(pandigital_list)

print "Took %s seconds to find sum of unique pandigitals: %s" % (end_time - start_time,sum(unique_pandigitals))
print "The list of unique pandigitals is %s" % (unique_pandigitals)




