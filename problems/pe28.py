"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Brute Force:
Notice that the first number in the spiral is at index = 0, then the next is at index = 2, and the next at index = 4.
In fact, here are the indices of the first 4 levels of the spiral:

L0 = 0
L1 = 2, 4, 6, 8
L2 = 12, 16, 20, 24
L3 = 30, 36, 42, 48

See a pattern?
L1 has a difference of 2, L2 has a difference of 4, L2 has a difference of 6, etc.
And each level has exactly 4 elements.
So basically, you increment the difference by 2 every single level
"""

import time


def return_index_values_for_spiral_length_dimension(spiral_length_dimension):
    diagonal_number_count = 2 * spiral_length_dimension - 1
    index_values = [0]
    last_increment_value = 2
    while index_values.__len__() < diagonal_number_count:
        last_index_value_for_previous_level = index_values[index_values.__len__() - 1]
        for diagonal_counter in range(1, 5):
            index_values.append(last_index_value_for_previous_level + diagonal_counter * last_increment_value)
        last_increment_value += 2
    return index_values


def calculate_diagonal_sum(diagonal_index_values):
    numbers = [number for number in range(1, (((diagonal_index_values.__len__() + 1) / 2) ** 2) + 1)]
    diagonal_sum = 0
    for diagonal_index_value in diagonal_index_values:
        diagonal_sum += numbers[diagonal_index_value]
    return diagonal_sum


def main(spiral_length_dimension):

    start_time = time.time()

    index_values = return_index_values_for_spiral_length_dimension(spiral_length_dimension)
    diagonal_sum = calculate_diagonal_sum(index_values)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "diagonal sum is {0} for spiral with length {1}; execution took {2} seconds".format(diagonal_sum, spiral_length_dimension, execution_seconds)


main(1001)