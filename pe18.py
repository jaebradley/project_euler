'''
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

import os as os
cwd = os.getcwd() #get current directory
d = {} #dictionary of values
with open(cwd + '/pe18') as raw_file:
    row = 0
    for line in raw_file:
        converted_list = [int(x) for x in line.split()] #convert strings to ints
        d[row] = converted_list #dictionary key is "row" number
        row += 1

dlen = len(d)
#from index of last row, in this case, length of dictionary - 1, iterate through row, except first row, to find max value of each pair
for row in range(dlen - 1,0,-1):
    rlen = len(d[row])
    for index in range(0,rlen - 1): #for each pair of values get max, since we are getting pairs the first index value is from 0 to row length - 1
        index_pair = index + 1
        first_num = d[row][index]
        sec_num = d[row][index_pair]
        max_num = max(first_num,sec_num)
        parent_value = d[row - 1][index] #parent value
        new_parent_value = max_num + parent_value
        d[row - 1][index] = new_parent_value #replace parent value with new value

print d #max value will be found at key = 0
