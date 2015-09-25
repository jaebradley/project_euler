"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
from utils.sieve_of_atkin import SieveOfAtkin

# I chickened out and used a 3rd party prime sieve


def sum_primes(limit):
    result_sum = 0
    sieve = SieveOfAtkin(limit)
    primes = sieve.getPrimes()
    for prime in primes:
        result_sum += prime
    return result_sum


def main():
    start_time = time.time()

    sum_of_primes = sum_primes(2000000)

    end_time = time.time()
    execution_time_in_seconds = end_time - start_time
    print "sum of primes is {0}; executed in {1} seconds".format(sum_of_primes, execution_time_in_seconds)

main()