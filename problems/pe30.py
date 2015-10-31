"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

# From http://www.mathblog.dk/project-euler-30-sum-numbers-that-can-be-written-as-the-sum-fifth-powers-digits/
# So lets determine the upper bound. We need to find a number x*95 which gives us an x digit number.
# We can do this by hand. Since 95 = 59049, we need at least 5 digits. 5*95 = 295245, so with 5 digits we can make a 6 digit number.
# 6*95 = 354294. So 355000 seems like a reasonable upper bound to use. We could probably tighten is even further if we wanted.


import time


def return_sum_of_all_numbers_that_can_be_written_as_fifth_powers_of_their_digits():
    number_sum = 0
    for number in range(2, 3550001):
        digit_sum = 0
        for digit in str(number):
            digit_sum += int(digit) ** 5
        if digit_sum == number:
            number_sum += number
    return number_sum


# TODO: solution takes a long ass time, optimize in future
def main():
    start_time = time.time()

    number_sum = return_sum_of_all_numbers_that_can_be_written_as_fifth_powers_of_their_digits()

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "the sum of all numbers that can be written as 5th power of their digits is {0}; execution took {1} seconds".format(number_sum, execution_seconds)


main()