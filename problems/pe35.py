'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?


TOO SLOW ~150 seconds, but can't think of anything that optimizes right now
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
    return sorted(numpy.r_[2,result])

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
    return tuple(sorted(digit_list)),digit_list

start_time = time.time()
primes = sieve(1000000)
primes2 = sieve(9999999)
circular_primes_dict = {}
circular_primes_list = []

for prime in primes:
    if prime > 100:
        print prime
        digit_data = getDigits(prime)
        key_number = prime
        digit_list = digit_data[1]
        new = 1
        is_circular = 1
        for digit in digit_list:
            if (digit % 2 == 0) or (digit % 5 == 0):
                circular_primes_dict[key_number] = {'value':0,'numbers':[prime]}
                is_circular = 0
                break
        if is_circular == 1:
            for key in circular_primes_dict:
                if key_number in circular_primes_dict[key]['numbers']:
                    new = 0
                    break
            if new == 1:
                circular_primes_dict[key_number] = {'value':1,'numbers':[prime]}
                for i in range(0,len(digit_list) - 1):
                    digit = digit_list.pop(-1)
                    digit_list = [digit] + digit_list
                    number = int(''.join(str(dig) for dig in digit_list))
                    circular_primes_dict[key_number]['numbers'].append(number)
                    if is_prime(number,primes2) == 0:
                        circular_primes_dict[key_number]['value'] = 0

for key in circular_primes_dict:
    if circular_primes_dict[key]['value'] == 1:
        for number in circular_primes_dict[key]['numbers']:
            circular_primes_list.append(number)

unique_circular_primes = set(circular_primes_list)
answer = len(unique_circular_primes) + 13
end_time = time.time()
seconds = end_time - start_time
print "Took %s seconds to find answer: %s" % (seconds, answer)







