# coding=utf-8
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time
from utils.utilities import is_palindrome

# Brute force approach of for looping through all 3-digit numbers
# However, one would suspect that the largest palindromes should be found when both numbers are closest to 1000.
# Which means, for loops should start from 1000 and go to 100
# One trick is that there is no need to double-compute products.
# For example, if we've computed the product of 100 x 101 then there is no reason to compute 101 x 100


def find_largest_palindrome_product():
    largest_palindrome = 0
    for first_number in range(1000, 100):
        for second_number in range(first_number, 100):  # note how the second for loop's range is floored
            product = first_number * second_number
            if product > largest_palindrome:
                if is_palindrome(product):
                    largest_palindrome = product
    return largest_palindrome

# Same brute force approach, but adding a basic initial string checker to reduce the number of cases to fully test


def find_largest_palindrome_product_v2():
    largest_palindrome = 0
    for first_number in range(1000, 100):
        for second_number in range(first_number, 100):  # note how the second for loop's range is floored
            product = first_number * second_number
            if product > largest_palindrome:
                stringified_product = str(product)
                stringified_product_length = stringified_product.__len__()
                if stringified_product[0] == stringified_product[stringified_product_length - 1]:
                    if is_palindrome(product):
                        largest_palindrome = product
    return largest_palindrome


def main():
    first_run_start_time = time.time()

    first_run_largest_palindrome_product = find_largest_palindrome_product()

    first_run_end_time = time.time()
    first_run_execution_time_in_seconds = first_run_end_time - first_run_start_time
    print "basic version: largest palindrome made from the product of two 3-digit numbers is {0}; execution time in seconds: {1}".\
        format(first_run_largest_palindrome_product, first_run_execution_time_in_seconds)

    second_run_start_time = time.time()

    second_run_largest_palindrome_product = find_largest_palindrome_product_v2()

    second_run_end_time = time.time()
    second_run_execution_time_in_seconds = second_run_end_time - second_run_start_time
    print "v2: largest palindrome made from the product of two 3-digit numbers is {0}; execution time in seconds: {1}".\
        format(second_run_largest_palindrome_product, second_run_execution_time_in_seconds)

main()