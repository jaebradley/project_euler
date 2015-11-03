"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from __future__ import division
import time


def is_naive_non_trivial_simplification(numerator, denominator):
    # assuming all numerators and denominators are 2-digit values
    numerator_string = str(numerator)
    denominator_string = str(denominator)
    tens_digit_numerator = int(numerator_string[0])
    ones_digit_numerator = int(numerator_string[1])
    tens_digit_denominator = int(denominator_string[0])
    ones_digit_denominator = int(denominator_string[1])

    # check that none of the ones digits are 0 -- this is the trivial case
    if (0 == ones_digit_numerator) or (0 == ones_digit_denominator):
        return False

    if tens_digit_numerator == tens_digit_denominator and 1 != ones_digit_numerator / ones_digit_denominator:
        candidate_value = ones_digit_numerator / ones_digit_denominator

    elif tens_digit_numerator == ones_digit_denominator and 1 != ones_digit_numerator / tens_digit_denominator:
        candidate_value = ones_digit_numerator / tens_digit_denominator

    elif ones_digit_numerator == tens_digit_denominator and 1 != tens_digit_numerator / ones_digit_denominator:
        candidate_value = tens_digit_numerator / ones_digit_denominator

    elif ones_digit_numerator == ones_digit_denominator and 1 != tens_digit_denominator / tens_digit_numerator:
        candidate_value = tens_digit_denominator / tens_digit_numerator

    else:
        return False

    if candidate_value == numerator / denominator:
        return True
    else:
        return False


def return_sum_of_naive_non_trivial_simplification_denominators():
    denominators = list()
    for candidate_numerator in range(10, 100):
        for candidate_denominator in range(candidate_numerator + 1, 100):
            if is_naive_non_trivial_simplification(numerator=candidate_numerator, denominator=candidate_denominator):
                denominators.append(candidate_denominator)
    return sum(denominators)


def main():
    start_time = time.time()

    denominator_sum = return_sum_of_naive_non_trivial_simplification_denominators()

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "sum of denominators is {0}; execution took {1} seconds".format(denominator_sum, execution_seconds)


main()