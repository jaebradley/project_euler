'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

1. Find all primes below 1 million
2. For length of prime, rearrange prime by adding first value to end
3. Evaluate if prime, if not, end
4. If counter is equal to length of prime then the prime is a circular prime
5. All primes can't contain a 2

TOO SLOW
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
    return digit_list

def checkCircularNumbers(digit_list):
    is_circular_number = 1
    all_numbers = []
    if (5 in digit_list) or (0 in digit_list) or (2 in digit_list) or (4 in digit_list) or (6 in digit_list) or (8 in digit_list):
        is_circular_number = 0
    for i in range(0,len(digit_list) - 1):
        digit = digit_list.pop(-1)
        digit_list = [digit] + digit_list
        number = int(''.join(str(dig) for dig in digit_list))
        all_numbers.append(number)
        if 1 == is_circular_number:
            if (0 == number % 2) or (0 == number % 5) or (not is_prime(number,prime_list2)) :
                is_circular_number = 0
    return is_circular_number,tuple(all_numbers)

def primeNotInCache(circular_numbers_tuple,is_circular,cached_map):
    for number in circular_numbers_tuple:
        if number not in cached_map:
            cached_map[number] = is_circular


prime_list = sieve(1000000)
cached_map = {}
prime_list2 = sieve(2000000)

for prime in prime_list:
    if (prime >= 100) and (prime not in cached_map):
        digit_list = getDigits(prime)
        circular_number_results = checkCircularNumbers(digit_list)
        is_circular = circular_number_results[0]
        all_circular_numbers = circular_number_results[1]
        primeNotInCache(all_circular_numbers,is_circular,cached_map)
circular_list = []
for key in cached_map:
    if cached_map[key] == 1:
        circular_list.append(key)

print circular_list,len(circular_list)


