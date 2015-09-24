# coding=utf-8
__author__ = 'jaebradley'
'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''

import time
import math

start_time = time.time()
combinations_list = []

for r in range(1,100):
    for n in range(r + 1, 101):
        combinations = math.factorial(n)/(math.factorial(r) * (math.factorial(n-r)))
        if combinations > 1000000:
            combinations_list.append(combinations)

answer = len(combinations_list)
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s" % (run_time, answer)