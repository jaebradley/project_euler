# coding=utf-8
__author__ = 'jaebradley'
import numpy as numpy
import time

def getDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return digit_list

def is_pandigital(number):
    digit_list = getDigits(number)
    if (max(digit_list) != len(digit_list)) or (min(digit_list) != 1):
        return 0
    else:
        for i in range(1,len(digit_list) + 1):
            try:
                digit_list.remove(i)
            except ValueError:
                return 0
        if not digit_list:
            return 1
        else:
            return 0

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
    return sorted(numpy.r_[2,result])

def is_prime(test,prime_list):
    i = 0
    while prime_list[i] <= test:
        if prime_list[i] == test:
            return 1
        else:
            i += 1
    return 0

def return_largest_pandigital_prime(prime_list):
    for i in range(len(prime_list) - 1,0,-1):
        prime = prime_list[i]
        if is_pandigital(prime) == 1:
            return prime

start_time = time.time()
prime_list = sieve(7654321)
'''
Why start with 7654321?

1+2+3+4+5+6+7+8+9 = 45

1+2+3+4+5+6+7+8 = 36

1+2+3+4+5+6+7 = 28

1+2+3+4+5+6 = 21

1+2+3+4+5 = 15

1+2+3+4 = 10

1+2+3 = 6

1+2 = 3

From here it is pretty clear that all pandigital numbers except 4 and 7 digit ones are divisible by 3 and thus can’t be primes.
'''

print "now looping through prime list"
prime = return_largest_pandigital_prime(prime_list)
end_time = time.time()
diff_seconds = end_time - start_time
print "Took %s seconds and found %s" % (diff_seconds, prime)