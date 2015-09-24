# coding=utf-8
from utils import project_euler_helpers as pe

__author__ = 'jaebradley'
'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

Brute Force Strategy:

1.  First thought about how to get diagonal numbers.
    Note that the bottom right diagonal number is always side length ** 2 and that the side length is always an odd number
    and obviously only 4 diagonal numbers per side length.
2.  So to get diagonal numbers for a given side length, find side length ** 2
    and subtract (side length - 1) from that, set the answer as the "new" side length and subtract (side length - 1) from that,
    then set the answer as the "new" side length, etc. Do this process three times and each time append the answer to
    a diagonal numbers list that is returned at the end of the function
3.  Next, thought about larger process outside diagonal number getter.
    Create an all diagonals list that contains 1. Create a prime count set to 0.
    Iterate through odd numbers from 3 to 100000 (didn't come up with an upper bound, so used an arbitrarily large one) to get side length.
    Get the diagonals for given side length.
    Loop through those diagonals (this process is inefficient) and if diagonal is prime then increment prime count by 1.
    If prime count/length(all diagonals list) < 0.1 then print the current side length, which is the answer, and break out of the for loop
'''
import time as time
from decimal import *

def getDiagonals(side_length):
    last_number = side_length ** 2
    diagonals_list = [last_number]
    for i in range(0,3):
        number = last_number - (side_length- 1)
        diagonals_list.append(number)
        last_number = number
    return diagonals_list

start_time = time.time()
all_diagonals = [1]
prime_count = 0
answer = "didn't resolve"
for length in range(3,1000000,2):
    diagonals = getDiagonals(length)
    for diagonal in diagonals:
        all_diagonals.append(diagonal)
        if pe.prime_test(diagonal):
            prime_count += 1
    print "Prime Ratio is %s for square length %s." % (round(Decimal(prime_count)/Decimal(len(all_diagonals)),4),length)
    if Decimal(prime_count)/Decimal(len(all_diagonals)) < 0.1:
        answer = length
        break
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s." % (run_time,answer)

