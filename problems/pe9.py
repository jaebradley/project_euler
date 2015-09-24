"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2^
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time

# brute force
# note the range ceilings: if a is 1 then the most that b could be is 499 if a < b < c (since c would be 500)


def find_pythagorean_triplet_product():
    for a in range(1, 299):
        for b in range(a + 1, 499):
            c = 1000 - b - a
            if c ** 2 == b ** 2 + a ** 2:
                return a * b * c


def main():
    start_time = time.time()

    product = find_pythagorean_triplet_product()

    end_time = time.time()

    execution_time_in_seconds = end_time - start_time

    print "product is {0}; execution time in {1} seconds".format(product, execution_time_in_seconds)

main()