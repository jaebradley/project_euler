"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

import time
from utils.is_prime import is_prime


def nth_prime(n):
    counter = 0
    number = 0
    while counter <= n:
        number += 1
        if is_prime(number):
            counter += 1
    return number


def main(limit):
    start_time = time.time()

    prime_number = nth_prime(limit)

    end_time = time.time()
    execution_time_in_seconds = end_time - start_time

    print "the {0}th prime number is {1}; execution took {2} seconds".format(limit, prime_number, execution_time_in_seconds)

main(10001)