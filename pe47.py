# coding=utf-8
__author__ = 'jaebradley'

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

Brute Force Solution (takes around 41 seconds):

1. 2 * 3 * 5 * 7 must be lower bound, but use million as upper bound (not a great strategy)
2. I iterate through all integers between lower and upper bound and count the number of prime factors
3. Log the results in dictionary
4. Loop through dictionary to get all numbers which have exactly 4 prime factors, put numbers in sorted list
5. Loop through list to get first 4 consecutive integers
'''
import numpy
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

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def generatePrimeFactorDictionary(start_number, end_number):
    prime_factor_count_dict = {}
    for number in range(start_number,end_number):
        prime_factors = primes(number)
        unique_prime_factors = set(prime_factors)
        if len(unique_prime_factors) == 4:
            prime_factor_count_dict[number] = 1
        else:
            prime_factor_count_dict[number] = 0
    return prime_factor_count_dict

def generateSortedPrimeFactorList(prime_factor_dictionary):
    prime_factor_count_list = []
    for key in prime_factor_dictionary:
        if prime_factor_dictionary[key] == 1:
            prime_factor_count_list.append(key)
    return sorted(prime_factor_count_list)

def findConsecutiveNumbers(prime_factor_count_list):
    for i in range(0,len(prime_factor_count_list) - 4):
        number = prime_factor_count_list[i]
        number2 = prime_factor_count_list[i+1]
        number3 = prime_factor_count_list[i+2]
        number4 = prime_factor_count_list[i+3]
        if (number2 - number == 1) and (number3 - number == 2) and (number4 - number == 3):
            answer = number
            return answer

start_time = time.time()
start_number = 2 * 3 * 5 * 7
prime_factor_count_dict = generatePrimeFactorDictionary(start_number,1000000)
prime_factor_count_list = generateSortedPrimeFactorList(prime_factor_count_dict)
answer = findConsecutiveNumbers(prime_factor_count_list)
end_time = time.time()
run_time = end_time - start_time
print "Solution found in %s seconds -- the answer is %s" % (run_time,answer)