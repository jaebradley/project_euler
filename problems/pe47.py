# coding=utf-8

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

Brute force:

Iterate through numbers until inputted forced upper limit
If at any point before reaching the upper limit, the length of the distinct prime factors for all of the four consecutive integers is 4 then return the first integer

Took 41 seconds before, now takes ~3 seconds.  Not the best, but the best simple solution I can think of
"""

from utils.utilities import return_distinct_prime_factors
import time


def return_first_integer_of_four_consecutive_integers_with_four_distinct_prime_factors(break_at_upper_limit):
    first_integer = 1
    while first_integer < break_at_upper_limit:
        second_integer = first_integer + 1
        third_integer = first_integer + 2
        fourth_integer = first_integer + 3
        if 4 == len(return_distinct_prime_factors(number=first_integer))\
            == len(return_distinct_prime_factors(number=second_integer))\
            == len(return_distinct_prime_factors(number=third_integer))\
            == len(return_distinct_prime_factors(number=fourth_integer)):
            return first_integer

        first_integer += 1
    return None


def main(break_at_upper_limit):
    start_time = time.time()

    first_integer = return_first_integer_of_four_consecutive_integers_with_four_distinct_prime_factors(break_at_upper_limit=break_at_upper_limit)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "The first integer of four consecutive integers with four distinct prime factors is {0}; took {1} seconds".format(first_integer, execution_seconds)


main(1000000000)
