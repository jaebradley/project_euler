'''
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import numpy as numpy
def sieve(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[       p*p//3     ::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]

#test if inputed number is prime
def is_prime(test):
    i = 0
    while prime_list[i] <= test:
        if prime_list[i] == test:
            return 1
        else:
            i += 1
    return 0

#give me all the double squares less than a specified number
def double_squares(number):
    double_square_list = list()
    for a in range(0,number):
        double_square = 2 * (a ** 2)
        if double_square < number:
            double_square_list.append(double_square)
        else:
            break
    return double_square_list

prime_list = sieve(1000000) # I'm assuming the smallest odd composite is less than 1M
prime_counter = 1 # dummy value so we can enter while
start = 3
while prime_counter != 0:
    print start
    double_square_list = double_squares(start)
    prime_counter = 0
    for a in range(0,len(double_square_list)):
        diff = start - double_square_list[a]
        if is_prime(diff):
            prime_counter += 1
    if prime_counter != 0:
        start += 2
    else:
        break





