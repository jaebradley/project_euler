'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Works but is slow -- should optimize in the future:
  1. No string parsing, just use modulo
  2. Rules like "if 2 digit number can't have a digit that's 5+ because 5! == 120 => 3 digits
  3. Cache all permutations of number -- so 145, 451, 541, 154, 415, 514, all will have factorial sum of 145
'''

import math as math
from timeit import default_timer as timer

def getSortedDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return tuple(sorted(digit_list))

def calculateFactorialOfDigits(digit_tuple):
    factorial_sum = 0
    for digit in digit_tuple:
        factorial_sum +=math.factorial(digit)
    return factorial_sum

def checkDigitListInCache(sorted_digit_tuple,cached_map):
    if sorted_digit_tuple not in cached_map:
        cached_map[sorted_digit_tuple] = [calculateFactorialOfDigits(sorted_digit_tuple) - sum(sorted_digit_tuple)]

fact_sum_dict = {}
start = timer()
for num in range(10,145):
    print num
    digit_tuple = getSortedDigits(num)
    checkDigitListInCache(digit_tuple,fact_sum_dict)
print fact_sum_dict
elapsed_time = round((timer() - start),2)
#print "Found %d in %r s" %(ans,elapsed_time)