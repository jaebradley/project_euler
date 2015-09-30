# coding=utf-8
"""
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math
import time


def return_sum_digits_of_number(number):
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    return digit_sum


def main(number):
    start_time = time.time()

    digit_sum = return_sum_digits_of_number(number)

    end_time = time.time()
    execution_seconds = end_time - start_time

    print "the digit sum is {0}; executed in {1} seconds".format(digit_sum, execution_seconds)

main(math.factorial(100))
