# coding=utf-8
"""
https://projecteuler.net/problem=72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

Took solution from: http://www.mathblog.dk/project-euler-72-reduced-proper-fractions/
Euler Totient Function: https://en.wikipedia.org/wiki/Euler%27s_totient_function
"""
from __future__ import division

limit = 1000000
phi = [x for x in range(0, limit + 1)]
result = 0

for i in range(2, limit + 1):
    if i == phi[i]:
        for j in range(i, limit + 1, i):
            phi[j] = (phi[j] / i) * (i - 1)

    result += phi[i]

print result