# coding=utf-8
"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time


def return_next_collatz_number(number):
    if 1 == number:
        raise ValueError("input number is one")
    if 0 == number % 2:
        collatz_transform = number / 2
    else:
        collatz_transform = 3 * number + 1
    return collatz_transform


def number_with_longest_collatz_chain(limit):
    collatz_number_chain_length_lookup = dict()
    longest_chain = 0
    longest_chain_number = 0
    for number in range(1, limit):
        chain_length = 0
        collatz_number = number
        while collatz_number > 1:
            if collatz_number in collatz_number_chain_length_lookup:
                chain_length += collatz_number_chain_length_lookup[collatz_number]
                collatz_number = 1  # kinda hacky, used to get out of loop
            else:
                collatz_number = return_next_collatz_number(collatz_number)
                chain_length += 1
        collatz_number_chain_length_lookup[number] = chain_length
        if chain_length > longest_chain:
            longest_chain = chain_length
            longest_chain_number = number
    return longest_chain_number


def main(limit):
    start_time = time.time()

    number = number_with_longest_collatz_chain(limit)

    end_time = time.time()
    execution_seconds = end_time - start_time

    print "{0} produces longest collatz chain under {1}; execution took  {2} seconds".format(number, limit, execution_seconds)

main(2000000)
