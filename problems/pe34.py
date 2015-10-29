'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Upper bound is 7 * 9! because 8 * 9! < 99,999,999
Additional qualification rules such as any two digit number with a digit that's 5+ can't be valid because 5! has more than 2 digits on it's own
Store the factorial values in a dictionary keyed on a sorted digit tuple so that I can quickly look up new numbers by their sorted digits
'''

import math as math
import time

def getSortedDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return tuple(sorted(digit_list)),digit_list

def calculateFactorialOfDigits(digit_tuple):
    factorial_sum = 0
    for digit in digit_tuple:
        factorial_sum +=math.factorial(digit)
    return factorial_sum

def checkForFactorialInCache(sorted_digit_tuple,cached_map):
    if sorted_digit_tuple not in cached_map:

        cached_map[sorted_digit_tuple] = {
            'value':calculateFactorialOfDigits(sorted_digit_tuple)
            }

    if (sorted_digit_tuple in cached_map):
        return cached_map[sorted_digit_tuple]['value']


start_time = time.time()
fact_sum_dict = {}
fact_sum_list = []
for num in range(10,2540160):
    digit_data = getSortedDigits(num)
    digit_tuple = digit_data[0]
    digit_list = digit_data[1]
    if (len(digit_list) == 2) and (max(digit_list) >= 5):
        continue
    elif (len(digit_list) == 3) and (max(digit_list) >= 7):
        continue
    elif (len(digit_list) == 4) and (max(digit_list) >= 8):
        continue
    elif (len(digit_list) == 5) and (max(digit_list) == 9):
        continue
    factorial_sum = checkForFactorialInCache(digit_tuple,fact_sum_dict)
    if num == factorial_sum:
        fact_sum_list.append(num)

total_sum = sum(fact_sum_list)

end_time = time.time()
time_diff = end_time - start_time
print "Answer is %s from list of %s. Took %s seconds to run" % (total_sum, fact_sum_list, time_diff)

