'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

TOO SLOW

748317
'''

import numpy as numpy
import time

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

def is_prime(test,prime_list):
    i = 0
    while prime_list[i] <= test:
        if prime_list[i] == test:
            return 1
        else:
            i += 1
    return 0

def getDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return digit_list

start_time = time.time()
prime_list = sieve(748317)
prime_list2 = sieve(10000000)
truncatable_primes = []
for prime in prime_list:
    if prime > 7:
        digit_list = getDigits(prime)
        forward_number_str = ''
        for digit in digit_list:
            forward_number_str = forward_number_str + str(digit)
            forward_number = int(forward_number_str)
            if (0 == is_prime(forward_number,prime_list2)):
                break
            elif (1 == is_prime(forward_number,prime_list2)) and (forward_number == prime):
                backward_number_str = ''
                for digit in reversed(digit_list):
                    backward_number_str = str(digit) + backward_number_str
                    backward_number = int(backward_number_str)
                    if (0 == is_prime(backward_number,prime_list2)):
                        break
                    elif (1 == is_prime(backward_number,prime_list2)) and (backward_number == prime):
                        truncatable_primes.append(prime)
                        print prime
    if len(truncatable_primes) == 11:
        break
end_time = time.time()
print truncatable_primes, sum(truncatable_primes)
print "Took %s seconds" % (end_time - start_time)