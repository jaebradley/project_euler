# coding=utf-8
"""
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

import time
import math


def return_next_numerator(previous_numerator, previous_denominator):
    return previous_numerator + 2 * previous_denominator


def return_next_denominator(previous_denominator, twice_previous_denominator):
    return 2 * previous_denominator + twice_previous_denominator


def return_digit_count(number):
    return int(math.log10(number) + 1)


def return_larger_numerator_count(max_number_of_expansions):
    previous_numerator = 1
    previous_denominator = 1
    twice_previous_denominator = 0
    expansion_counter = 0
    longer_numerator_counter = 0

    while expansion_counter <= max_number_of_expansions:
        next_numerator = return_next_numerator(previous_numerator, previous_denominator)
        next_denominator = return_next_denominator(previous_denominator, twice_previous_denominator)
        if return_digit_count(next_numerator) > return_digit_count(next_denominator):
            longer_numerator_counter += 1
        twice_previous_denominator = previous_denominator
        previous_denominator = next_denominator
        previous_numerator = next_numerator
        expansion_counter += 1

    return longer_numerator_counter


def main(max_number_of_expansions):
    start_time = time.time()

    counter = return_larger_numerator_count(max_number_of_expansions)

    end_time = time.time()

    execution_seconds = end_time - start_time

    print "{0} fractions where the numerator has more digits than the denominator in the first {1} expansions; executed in {2} seconds".format(counter, max_number_of_expansions, execution_seconds)


main(1000)