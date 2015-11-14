# coding=utf-8
"""
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Why start with 7654321?

1+2+3+4+5+6+7+8+9 = 45

1+2+3+4+5+6+7+8 = 36

1+2+3+4+5+6+7 = 28

1+2+3+4+5+6 = 21

1+2+3+4+5 = 15

1+2+3+4 = 10

1+2+3 = 6

1+2 = 3

From here it is pretty clear that all pandigital numbers except 4 and 7 digit ones are divisible by 3 and thus can’t be primes.
"""
import time
from utils.utilities import is_pandigital, sieve


def return_largest_pandigital_prime(upper_limit):
    primes = sieve(n=upper_limit)
    for prime in reversed(primes):
        if is_pandigital(candidate_number=prime):
            return prime


def main(upper_limit):
    start_time = time.time()

    largest_pandigital_prime = return_largest_pandigital_prime(upper_limit=upper_limit)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "largest pandigital prime is {0}; took {1} seconds".format(largest_pandigital_prime, execution_seconds)


main(upper_limit=7654321)
