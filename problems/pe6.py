# coding=utf-8
"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import time


def sum_of_first_n_natural_numbers_squared(n):
    squared_sum = 0
    for natural_number in range(1, n + 1):
        squared_sum += natural_number ** 2
    return squared_sum


def square_of_sum_of_first_n_natural_numbers(n):
    sum_of_natural_numbers = 0
    for natural_number in range(1, n + 1):
        sum_of_natural_numbers += natural_number
    return sum_of_natural_numbers ** 2


def main():
    start_time = time.time()

    first_100_natural_numbers = sum_of_first_n_natural_numbers_squared(100)
    sum_of_first_100_natural_numbers_squared = square_of_sum_of_first_n_natural_numbers(100)

    difference = abs(sum_of_first_100_natural_numbers_squared - first_100_natural_numbers)

    end_time = time.time()
    execution_time_in_seconds = end_time - start_time
    print "difference is {0}; execution time in seconds: {1}".format(difference, execution_time_in_seconds)

main()