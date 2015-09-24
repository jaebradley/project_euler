"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

# Brute force
# Loop through range and utilize modulo to determine if a number is a multiple of 3 or 5

start_time = time.time()

total_sum = 0

for natural_number in range(1, 1000):
    if (0 == natural_number % 3) or (0 == natural_number % 5):
        total_sum += natural_number

end_time = time.time()
elapsed_time = end_time - start_time

print "sum of all multiples of 3 or 5 below 1000 is {0}, execution time (in seconds): {1}".format(total_sum, elapsed_time)