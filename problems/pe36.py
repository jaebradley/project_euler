"""
https://projecteuler.net/problem=36
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from utils.utilities import is_palindrome
import time


def return_base_two_representation(base_10_number):
    number, multiplier = 0, 1
    while base_10_number > 0:
        number += base_10_number % 2 * multiplier
        multiplier *= 10
        base_10_number /= 2
    return number


def return_base_2_and_base_10_palindrome_sum(limit):
    double_palindrome_sum = 0
    for candidate in range(1, limit + 1):
        if is_palindrome(return_base_two_representation(base_10_number=candidate)) and is_palindrome(candidate):
            double_palindrome_sum += candidate
    return double_palindrome_sum


def main(limit):
    start_time = time.time()

    double_palindrome_sum = return_base_2_and_base_10_palindrome_sum(limit=limit)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "sum of double palindromes is {0}; took {1} seconds".format(double_palindrome_sum, execution_seconds)


main(limit=1000000)
