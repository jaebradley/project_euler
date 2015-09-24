'''
n^2 + an + b where |a| < 1000 and |b| < 1000
where |n| is the absolute value of n

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0

For a and b from -1000 to 1000 for increasing n, evaluate the function and evaluate if output is prime or not
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

def func(n,a,b):
    return n ** 2 + a * n + b

def is_prime(test):
    i = 0
    while prime_list[i] <= test:
        if prime_list[i] == test:
            return 1
        else:
            i += 1
    return 0

prime_list = sieve(800000)
max_list = list([0,0,0,0])
b_list = sieve(1000)
for a in range(-1000,1001):
    for i in range(0,len(b_list)):
        b = b_list[i]
        n = 0
        result = func(n,a,b)
        while is_prime(result) == 1:
            result = func(n,a,b)
            if is_prime(result) == 0:
                break
            n += 1
        if n > max_list[3]:
            max_list = ([a,b,a * b,n])

print max_list



