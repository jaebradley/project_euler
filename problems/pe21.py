# coding=utf-8
"""
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time


class AmicableNumber:
    def __init__(self, first_amicable_pair, second_amicable_pair):
        self.first_amicable_pair = first_amicable_pair
        self.second_amicable_pair = second_amicable_pair


# TODO: this is a pretty terrible way of calculating proper divisors so figure out a way to optimize in the future
def return_proper_divisor_sum_for_number(number):
    divisor_sum = 0
    for candidate_divisor in range(1, number):
        if 0 == number % candidate_divisor:
            divisor_sum += candidate_divisor
    return divisor_sum


def return_amicable_number(number):
    amicable_number_result = None
    divisor_sum_for_number = return_proper_divisor_sum_for_number(number)
    amicable_pair_candidate = return_proper_divisor_sum_for_number(divisor_sum_for_number)
    if number == amicable_pair_candidate and number != divisor_sum_for_number:
        amicable_number_result = AmicableNumber(number, divisor_sum_for_number)
    return amicable_number_result


def return_sum_of_amicable_numbers_less_than_limit_inclusive(limit):
    assert limit > 0

    amicable_number_list = list()
    for candidate_amicable_number in range(0, limit):
        if candidate_amicable_number not in amicable_number_list:
            amicable_number = return_amicable_number(candidate_amicable_number)
            if isinstance(amicable_number, AmicableNumber):
                amicable_number_list.append(amicable_number.first_amicable_pair)
                amicable_number_list.append(amicable_number.second_amicable_pair)
    return sum(amicable_number_list)


def main(limit):
    start_time = time.time()
    amicable_number_sum = return_sum_of_amicable_numbers_less_than_limit_inclusive(limit)
    end_time = time.time()
    execution_time = end_time - start_time
    print "the sum of amicable numbers under {0} is {1}; calculation took {2} seconds".format(limit, amicable_number_sum, execution_time)

main(10000)