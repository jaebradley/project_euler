# coding=utf-8
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math
import time


def return_number_digit_count(number):
    digit_count = int(math.log10(number))+1
    return digit_count


def return_index_of_the_first_fibonacci_number_with_digit_count_limit(fibonacci_digit_limit):
    # store initial fibonacci numbers
    fibonacci_numbers = [1, 1]
    next_fibonacci_number = 2
    fibonacci_number_index_value = 2
    while return_number_digit_count(next_fibonacci_number) < fibonacci_digit_limit:
        next_fibonacci_number = sum(fibonacci_numbers[-2:])
        fibonacci_number_index_value += 1
        fibonacci_numbers.append(next_fibonacci_number)
    return fibonacci_number_index_value


def main(fibonacci_digit_limit):
    start_time = time.time()

    fibonacci_number_index_value = return_index_of_the_first_fibonacci_number_with_digit_count_limit(fibonacci_digit_limit)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "index value for first Fibonacci number to contain {0} digits is {1}; execution took {2} seconds".format(fibonacci_digit_limit, fibonacci_number_index_value, execution_seconds)


main(1000)