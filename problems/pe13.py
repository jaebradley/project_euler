"""
https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import time


def convert_text_file_to_list_of_integers(file_path):
    output_list_of_strings = open(file_path).read().split()
    output_list_of_integers = map(int, output_list_of_strings)  # convert string objects to integers
    return output_list_of_integers


def main(file_path):
    start_time = time.time()

    integer_list = convert_text_file_to_list_of_integers(file_path)
    result_sum = sum(integer_list)
    result_string = str(result_sum)[:10]

    end_time = time.time()
    execution_time_in_seconds = end_time - start_time

    print "first ten digits are {0}; took {1} seconds".format(result_string, execution_time_in_seconds)

main("../static/pe13.txt")
