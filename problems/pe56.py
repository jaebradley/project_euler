"""
https://projecteuler.net/problem=56

A googol (10 ** 100) is a massive number: one followed by one-hundred zeros; 100 ** 100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a ** b, where a, b < 100, what is the maximum digital sum?
"""

from utils import project_euler_helpers as pe
import time


def return_greatest_digit_sum_for_a_and_b(a_limit_inclusive, b_limit_inclusive):
    greatest_digit_sum = 0
    for a in range(a_limit_inclusive, 0, -1):
        for b in range(b_limit_inclusive, 0, -1):
            digit_sum = sum(pe.getDigits(a ** b))
            if digit_sum > greatest_digit_sum:
                greatest_digit_sum = digit_sum
    return greatest_digit_sum


def main(a_limit_inclusive, b_limit_inclusive):
    start_time = time.time()

    greatest_digit_sum = return_greatest_digit_sum_for_a_and_b(
        a_limit_inclusive=a_limit_inclusive,
        b_limit_inclusive=b_limit_inclusive
    )

    end_time = time.time()
    execution_seconds = end_time - start_time

    print "greatest digit sum is {0}; took {1} seconds".format(greatest_digit_sum, execution_seconds)

main(100, 100)