"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import time
import math
from utils.is_prime import is_prime


def largest_prime_factor(number):
    square_root = int(math.floor(math.sqrt(number)))
    for potential_prime_factor in range(square_root, 1, -1):
        if is_prime(potential_prime_factor):
            return potential_prime_factor


def main(number):
    start_time = time.time()

    prime_factor = largest_prime_factor(number)

    end_time = time.time()
    execution_time_in_seconds = end_time - start_time

    print "largest prime factor of {0} is {1}; took {2} seconds".format(number, prime_factor, execution_time_in_seconds)

main(600851475143)