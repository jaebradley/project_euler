# coding=utf-8
"""
https://projecteuler.net/problem=53

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
"""

import time
import math


def return_number_of_conbinations(n, r):
    return math.factorial(n)/(math.factorial(r) * (math.factorial(n-r)))


def return_number_of_combinations_greater_than_limit_inclusive(limit_inclusive, n_upper_limit_inclusive):
    counter = 0
    for r in range(1, n_upper_limit_inclusive):
        for n in range(r + 1, n_upper_limit_inclusive + 1):
            if return_number_of_conbinations(n=n, r=r) > limit_inclusive:
                counter += 1
    return counter


def main(limit_inclusive, n_upper_limit_inclusive):
    start_time = time.time()

    number_of_combinations = return_number_of_combinations_greater_than_limit_inclusive(
        limit_inclusive=limit_inclusive,
        n_upper_limit_inclusive=n_upper_limit_inclusive
    )

    end_time = time.time()
    execution_seconds = end_time - start_time

    print "number of combinations greater than {0} is {1}; took {2} seconds".format(limit_inclusive, number_of_combinations, execution_seconds)

main(1000000, 100)