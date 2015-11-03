"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from __future__ import division


# num_log = []
#
# for z in range(11, 100):
#     for i in range(10, 100):
#             str_i = str(i)
#             str_z = str(z)
#             x0 = float(str_i[0])
#             x1 = float(str_i[1])
#             x2 = float(str_z[0])
#             x3 = float(str_z[1])
#             num = float(i)/float(z)
#             if x0 != 0.0 and x1 != 0.0 and x2 != 0.0 and x3 != 0.0:
#                 if x0 == x2 and x1/x3 < 1 and x1/x3 == num:
#                     num_log.append([i,z])
#                 elif x0 == x3 and x1/x2 < 1 and x1/x2 == num:
#                     num_log.append([i,z])
#                 elif x1 == x2 and x0/x3 < 1 and x0/x3 == num:
#                     num_log.append([i,z])
#                 elif x1 == x3 and x0/x2 < 1 and x0/x2 == num:
#                     num_log.append([i,z])
#
# print num_log


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

    # four possible combinations
    decimal_value = numerator / denominator

    # four possible candidate values
    candidate_value_1 = tens_digit_numerator / tens_digit_denominator
    candidate_value_2 = tens_digit_numerator / ones_digit_denominator
    candidate_value_3 = ones_digit_numerator / tens_digit_denominator
    candidate_value_4 = ones_digit_numerator / ones_digit_denominator

    # test candidate values
    if candidate_value_1 == decimal_value:
        return True
    elif candidate_value_2 == decimal_value:
        return True
    elif candidate_value_3 == decimal_value:
        return True
    elif candidate_value_4 == decimal_value:
        return True
    else:
        return False


def return_naive_non_trivial_simplification_denominators():
    denominators = list()
    for candidate_numerator in range(10, 100):
        for candidate_denominator in range(10, 100):
            if is_naive_non_trivial_simplification(numerator=candidate_numerator, denominator=candidate_denominator):
                denominators.append(candidate_denominator)
    return denominators

