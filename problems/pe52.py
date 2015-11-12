"""
https://projecteuler.net/problem=52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Brute Force Strategy:

1.  Iterate through all numbers
    (thought about instituting restriction that x must start with 1
    but I believe there are some corner cases where this doesn't work)
2.  Get all digits for each number as a list
3.  For a multiplier from 1 to 6, if the sorted digits of the product are the same
    as the sorted digits from the original number then "success" variable is 1, else it is 0
    and the inner for loop breaks in order to move on to the next number
4.  If success variable = 1 then assign i to answer variable and break outer for loop
    to stop iterating through numbers
"""

from utils import project_euler_helpers as pe
import time


def return_digit_comparison_for_multipliers(number, maximum_multiplier_value_inclusive):
    number_sorted_digits = sorted(pe.getDigits(number=number))
    for multiplier in range(2, maximum_multiplier_value_inclusive):
        if sorted(pe.getDigits(multiplier * number)) != number_sorted_digits:
            return False
    return True


def return_smallest_positive_integer_with_same_digit_multipliers(maximum_multiplier_value_inclusive):
    smallest_positive_integer = None
    number = 1
    while smallest_positive_integer is None:
        if return_digit_comparison_for_multipliers(number=number, maximum_multiplier_value_inclusive=maximum_multiplier_value_inclusive):
            return number

        number += 1


def main(maximum_multiplier_value_inclusive):
    start_time = time.time()

    smallest_positive_integer = return_smallest_positive_integer_with_same_digit_multipliers(maximum_multiplier_value_inclusive=maximum_multiplier_value_inclusive)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "smallest positive integer with same digits for multiples up to {0}x is {1}; took {2} seconds".format(
        maximum_multiplier_value_inclusive, smallest_positive_integer, execution_seconds
    )


main(6)