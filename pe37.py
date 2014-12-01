'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

TOO SLOW

748317
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
trunc_prime_list = list()
count = 0
while count < 10:
    if count == 10:
        break
    for a in range(4,len(prime_list)):
        prime = prime_list[a]
        prime_str = str(prime)
        prime_left_str = str(prime)
        prime_right_str = str(prime)
        dig = 0
        for b in range(0,len(prime_str) - 1):
            prime_left = int(prime_left_str[1:])
            prime_right = int(prime_right_str[:-1])
            if is_prime(prime_left) and is_prime(prime_right):
                prime_left_str = str(prime_left)
                prime_right_str = str(prime_right)
                dig += 1
            else:
                break
            if dig == len(prime_str) - 1:
                print prime,count
                trunc_prime_list.append(prime)
                count += 1

print trunc_prime_list
print sum(trunc_prime_list)

