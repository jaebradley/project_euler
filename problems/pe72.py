# coding=utf-8
"""
https://projecteuler.net/problem=72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

Took solution from: http://www.mathblog.dk/project-euler-72-reduced-proper-fractions/
Euler Totient Function: https://en.wikipedia.org/wiki/Euler%27s_totient_function
"""
from __future__ import division
import time


def return_reduced_proper_fraction_count_for_d(d_upper_limit_inclusive):
    """
    Basically, for each number from 2 to upper limit, divide any multiples by it,
    ensuring that any non-zero remaining numbers are count of all relatively prime divisors
    :param d_upper_limit_inclusive:
    :return:
    """
    phi = [x for x in range(0, d_upper_limit_inclusive + 1)]
    result = 0

    for i in range(2, d_upper_limit_inclusive + 1):
        if i == phi[i]:
            for j in range(i, d_upper_limit_inclusive + 1, i):
                phi[j] = (phi[j] / i) * (i - 1)

        result += phi[i]

    return result


def main(d_upper_limit_inclusive):
    start_time = time.time()

    reduced_proper_fraction_count = return_reduced_proper_fraction_count_for_d(
        d_upper_limit_inclusive=d_upper_limit_inclusive
    )

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "number of reduced proper fractions for d <= {0} is {1}; took {2} seconds".format(
        d_upper_limit_inclusive,
        reduced_proper_fraction_count,
        execution_seconds
    )

main(1000000)
