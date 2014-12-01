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
fact_sum_list = list()
start = timer()
for num in range(10,9999999):
    fact_sum = 0
    num_string = str(num)
    len_string = len(num_string)
    for a in range(0,len_string):
        digit = int(num_string[a])
        fact_sum += math.factorial(digit)
    if fact_sum == num:
        fact_sum_list.append(num)

ans = sum(fact_sum_list)
elapsed_time = round((timer() - start),2)
print "Found %d in %r s" %(ans,elapsed_time)