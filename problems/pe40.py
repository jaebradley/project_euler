"""
https://projecteuler.net/problem=40

Problem:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

Strategy:

1. Build string by starting with '1' and then adding consecutive integers until the string length (1,000,000) is met.
2. After concatenating integer, I check to see if the current string is greater than the string length --
    adding the next integer might make the string go from a length of 999,998 to a length of 1,000,002.
3. If this is the case, I simply get the first one million characters of the string.
4. For any given character position in the string, return the integer equivalent so that we can use them to multiply their values.
"""
import time


def return_fractional_string(length):
    fractional_string = str()
    for integer in range(1, length + 2):
        for digit in str(integer):
            if len(fractional_string) < length:
                fractional_string += digit
    return fractional_string


def return_product_of_fractional_digit_indices(fractional_string_length, *indices):
    fractional_string = return_fractional_string(length=fractional_string_length)
    fractional_digit_product = 1
    for index in indices:
       fractional_digit_product *= int(fractional_string[index - 1])
    return fractional_digit_product


def main(fractional_string_length):
    start_time = time.time()

    product = return_product_of_fractional_digit_indices(
        fractional_string_length,
        1,
        10,
        100,
        1000,
        10000,
        100000,
        1000000,
    )

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "product is {0}; took {1} seconds".format(product, execution_seconds)


main(1000000)
