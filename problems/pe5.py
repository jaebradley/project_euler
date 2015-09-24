"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Can calculate this without Python.

If a number is divisible by 20, that also implies that it is divisible by 10, 5, 4, 2, and 1.
If a number is divisible by 18, that also implies that it is divisible by 9, 6, 3, 2, and 1.

Basically, following this logic, if a number is divisible by numbers 20-11 it is also
divisible by numbers 10-1.

So now we need to find the LCD of the numbers 20-11.  Since 19, 17, 13, and 11 are prime numbers we really need to find
the LCD of 20, 18, 16, 15, 14, and 12 and multiply it by the aforementioned prime numbers to find the LCD of numbers
20-11.

Using prime factorization, one can discern that the LCD of the composite numbers between 20-11 is 2^4 * 3^2 * 5 * 7,
or 5040.  The product of 5040 and the primes between 20-11 is 232792560.
"""



