'''
https://projecteuler.net/problem=18

Problem 18:

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

1. Get dictionary of values {row -> value}; ex. {0 => 75, 1 => [95,64]}
2. For each row, starting from the last row, for every pair of values find the largest one and add it to it's parent from the previous row (image structure as tree) and replace the parent with that value.
2a. Example: in the last row, the first two elements, 04 and 62, map to the first element of the penultimate row, 63.
    Find the max of 04 and 62 (so, 62) and add it to 63 (125).
    Then, replace 63 with 125.
    Next, move on to 62 and 98 (which map to 66 in previous row).
    After completion of row, move on to row "above it"

'''

# Strategy to solve this problem involves starting at the very last row and working backwards
# For each pair of numbers in each row, they map to a parent number in the previous row
# Now, there's a maximum sum that can be calculated using the parent number and one of it's children
# You can imagine that if you follow this strategy from the last row to the first row,
# that the first element in the first row will be the maximum sum that can be calculated by taking adjacent steps from
# one row to the next

import time


def return_triangle_as_list_of_lists():
    pe18_txt = open("../static/pe18.txt")
    triangle_list = [[int(element) for element in list.split()] for list in pe18_txt]
    return triangle_list


def calculate_maximum_total(triangle_list_of_lists):
    for row in range(triangle_list_of_lists.__len__() - 1, 0, -1):
        for row_index in range(0, len(triangle_list_of_lists[row]) - 1, 1):
            max_value = max(triangle_list_of_lists[row][row_index], triangle_list_of_lists[row][row_index + 1])
            parent_value = triangle_list_of_lists[row - 1][row_index]
            new_parent_value = max_value + parent_value
            triangle_list_of_lists[row - 1][row_index] = new_parent_value

    return triangle_list_of_lists[0][0]


def main():
    start_time = time.time()

    triangle_list_of_lists = return_triangle_as_list_of_lists()
    maximum_total = calculate_maximum_total(triangle_list_of_lists)

    end_time = time.time()
    execution_seconds = end_time - start_time

    print "maximum total is {0}; executed in {1} seconds".format(maximum_total, execution_seconds)

main()