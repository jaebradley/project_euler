"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Brute Force:

1. Iterate from 1 to 28123
2. For each number find divisors (if too slow could try caching this step in dictionary)
3. If sum of divisors > than number then log into abundant number list
4. Iterate through every tuple in abundant number list where the tuple sum < 28123 and log into list
5. Iterate from 1 to 28213 and check if number is in tuple list
"""
from __future__ import division
import math
import time


def return_proper_divisors(number):
    divisors = list()
    square_root = int(math.floor(math.sqrt(number)))
    for candidate_divisor in range(1, square_root + 1):
        if number % candidate_divisor is 0:
            divisors.append(candidate_divisor)
            dividend = int(number / candidate_divisor)
            if dividend != number and dividend != square_root:
                divisors.append(dividend)
    return divisors


def is_abundant(number):
    divisors = return_proper_divisors(number=number)
    if sum(divisors) > number:
        return True
    else:
        return False


def return_abundant_numbers(limit_inclusive):
    amicable_numbers = list()
    for candidate_number in range(1, limit_inclusive + 1):
        if is_abundant(number=candidate_number):
            amicable_numbers.append(candidate_number)
    return amicable_numbers


def return_abundant_number_sums(limit_inclusive):
    amicable_number_sums = list()
    amicable_numbers = return_abundant_numbers(limit_inclusive=limit_inclusive)
    for first_amicable_number_index in range(0, len(amicable_numbers) - 1):
        for second_amicable_number_index in range(first_amicable_number_index + 1, len(amicable_numbers)):
            amicable_number_sum = amicable_numbers[first_amicable_number_index] + amicable_numbers[second_amicable_number_index]
            if amicable_number_sum <= limit_inclusive:
                amicable_number_sums.append(amicable_number_sum)
    return set(amicable_number_sums)


def return_sum_of_all_positive_integers_which_cannot_be_written_as_a_sum_of_two_abundant_numbers(limit_inclusive):
    abundant_number_sums = return_abundant_number_sums(limit_inclusive=limit_inclusive)
    numbers_that_cannot_be_written_as_a_sum_of_two_abundant_numbers = list()
    for candidate_number in range(1, limit_inclusive + 1):
        if candidate_number not in abundant_number_sums:
            numbers_that_cannot_be_written_as_a_sum_of_two_abundant_numbers.append(candidate_number)
    return sum(numbers_that_cannot_be_written_as_a_sum_of_two_abundant_numbers)


def main(limit_inclusive):
    start_time = time.time()

    sum_of_numbers_that_cannot_be_written_as_a_sum_of_two_abundant_numbers = return_sum_of_all_positive_integers_which_cannot_be_written_as_a_sum_of_two_abundant_numbers(
        limit_inclusive=limit_inclusive
    )

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "sum of numbers from 1 to {0} that cannot be written as two abundant numbers is {1}; took {2} seconds".format(
        limit_inclusive,
        sum_of_numbers_that_cannot_be_written_as_a_sum_of_two_abundant_numbers,
        execution_seconds
    )


main(limit_inclusive=28213)

