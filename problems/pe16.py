"""
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
"""

import time


def sum_of_digits(number):
    digit_sum = 0
    stringified_number = str(number)
    for index in range(0, stringified_number.__len__()):
        digit_sum += int(stringified_number[index])
    return digit_sum


def main(number):
    start_time = time.time()

    digit_sum = sum_of_digits(number)

    end_time = time.time()

    execution_seconds = end_time - start_time

    print "sum of digits for {0} is {1}; took {2} seconds".format(number, digit_sum, execution_seconds)

main(2 ** 1000)