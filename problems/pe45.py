"""
https://projecteuler.net/problem=45
Find the next triangle number that is also pentagonal and hexagonal greater than 40755
40755 is the 285th triangular number, the 165th pentagonal number, and the 144th hexagonal number

triangle number = n * (n + 1) / 2
pentagonal number = n * (3n - 1) / 2
hexagonal number = n * (2n - 1) /2
"""
import time


def is_triangle(number):
    """
    inverse function for triangular number
    :param number:
    :return:
    """
    return not (-1 + (1 + 8 * number) ** 0.5)/2 % 1


def is_pentagonal(number):
    """
    inverse function for pentagonal number
    :param number:
    :return:
    """
    return not (1 + (1 + 24 * number) ** 0.5)/6 % 1


def return_next_triangular_pentagonal_hexagonal_number(lower_bound_hexagonal_number_index_inclusive, upper_bound_hexagonal_number_index_inclusive):
    for hexagonal_number_index in range(lower_bound_hexagonal_number_index_inclusive, upper_bound_hexagonal_number_index_inclusive + 1):
        hexagonal_number = hexagonal_number_index * (2 * hexagonal_number_index - 1)
        if 1 == is_triangle(hexagonal_number) and 1 == is_pentagonal(hexagonal_number):
            return hexagonal_number


def main(lower_bound_hexagonal_number_index_inclusive, upper_bound_hexagonal_number_index_inclusive):
    start_time = time.time()

    next_triangular_pentagonal_hexagonal_number = return_next_triangular_pentagonal_hexagonal_number(
        lower_bound_hexagonal_number_index_inclusive=lower_bound_hexagonal_number_index_inclusive,
        upper_bound_hexagonal_number_index_inclusive=upper_bound_hexagonal_number_index_inclusive
    )

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "next number between hexagonal number indices {0} - {1} is {2}; took {3} seconds".format(
        lower_bound_hexagonal_number_index_inclusive,
        upper_bound_hexagonal_number_index_inclusive,
        next_triangular_pentagonal_hexagonal_number,
        execution_seconds
    )


main(
    lower_bound_hexagonal_number_index_inclusive=144,
    upper_bound_hexagonal_number_index_inclusive=100000
)

