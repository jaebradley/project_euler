from __future__ import division
"""
https://projecteuler.net/problem=63

The 5-digit number, 16807=7 ** 5, is also a fifth power. Similarly, the 9-digit number, 134217728=8 ** 9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import math


def return_digit_count(number):
    return int(math.log10(number) + 1)


def return_digit_power(number):
    digit_count = return_digit_count(number)
    return number ** digit_count


def is_n_digit_and_n_power(number):
    if return_digit_count(number) == return_digit_count(return_digit_power(number)):
        return True


def return_lower_bound(power):
    return int(math.ceil(10 ** ((power - 1) / power)))


def return_upper_bound(power):
    return int(math.ceil(10 ** power))

power = 1
counter = 0
lower_bound = 0
while lower_bound < 10:
    print lower_bound
    lower_bound = return_lower_bound(power)
    counter += 10 - lower_bound
    power += 1

print counter