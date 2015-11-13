"""
https://projecteuler.net/problem=46

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from __future__ import division
import math
import time
from utils.sieve_of_atkin import SieveOfAtkin
from utils.is_prime import is_prime


def is_candidate_value_sum_of_prime_and_twice_a_square(candidate_number, prime):
    candidate_square_value = (candidate_number - prime) / 2
    if math.sqrt(candidate_square_value).is_integer():
        return True

    return False


def return_smallest_odd_composite_that_cannot_be_written_as_sum_of_prime_and_twice_a_square(break_at_upper_limit_inclusive):
    for candidate_number in range(9, break_at_upper_limit_inclusive + 1, 2):
        if not is_prime(number=candidate_number):
            sieve = SieveOfAtkin(limit=candidate_number)
            primes = sieve.getPrimes()
            count_of_prime_sum_twice_square = 0
            for prime in primes:
                if is_candidate_value_sum_of_prime_and_twice_a_square(
                    candidate_number=candidate_number,
                    prime=prime
                ):
                    count_of_prime_sum_twice_square += 1

            if 0 == count_of_prime_sum_twice_square:
                return candidate_number


def main(break_at_upper_limit_inclusive):
    start_time = time.time()

    smallest_odd_composite = return_smallest_odd_composite_that_cannot_be_written_as_sum_of_prime_and_twice_a_square(
        break_at_upper_limit_inclusive=break_at_upper_limit_inclusive
    )

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "smallest odd composite is {0}; took {1} seconds".format(smallest_odd_composite, execution_seconds)


main(100000000)