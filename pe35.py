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
    return numpy.r_[2,result]

def is_prime(test):
    i = 0
    while prime_list[i] <= test:
        if prime_list[i] == test:
            return 1
        else:
            i += 1
    return 0

prime_list = sieve(1000000)
prime_list_v2 = list()
circular_primes = list()

for a in range(0,len(prime_list)):
    prime = prime_list[a]
    prime_str = str(prime)
    count = 0
    for b in range(0,len(prime_str)):
        if int(prime_str[b]) != 2 and int(prime_str[b]) != 4 and int(prime_str[b]) != 5 and int(prime_str[b]) != 6 and int(prime_str[b]) != 8:
            count += 1
    if count == len(prime_str) - 1:
        prime_list_v2.append(prime)

print len(prime_list_v2)

for a in range(0,len(prime_list_v2)):
    print a
    prime = prime_list_v2[a]
    prime_str = str(prime)
    count = 0
    if len(prime_str) > 1:
        for b in range(0,len(prime_str)):
            new_prime = prime_str[1:] + prime_str[0]
            prime_str = new_prime
            if is_prime(int(new_prime)) == 1:
                count += 1
            else:
                break
            if count == len(prime_str) - 1:
                circular_primes.append(prime)
    else:
        circular_primes.append(prime)

print len(circular_primes)


