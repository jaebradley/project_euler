'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Dynamic Programming/Brute Force Solution (Takes around 45 seconds)

1. Get list of the cumulative sum of primes.
   Looks something like [2, 5, 7, 14, 25,...]
   The reason we do this is that it then becomes easy to get sum of an arbitrary group of consecutive primes.
   The sum of the consecutive primes between 11 and 7 is really f(11), which equals 25, minus f(7), which is 14, which equals 11, which makes sense.
2. For each prime, check the sum of consecutive primes below it,
   and if the sum is prime and the length of consecutive sums is < the current longest length
   then update the current longest length and set the sum and length as the output values
'''


import numpy as numpy
import time
import math

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

def prime_test(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def getPrimesCumSum(prime_list):
    primes_cum_sum_list = []
    cum_sum = 0
    for prime in prime_list:
        cum_sum += prime
        primes_cum_sum_list.append(cum_sum)
    return primes_cum_sum_list

def findPrimeOfMostConsecutivePrimes(prime_list,primes_cum_sum_list,initial_most_consecutive,limit):
    longest = initial_most_consecutive
    prime_length = len(prime_list)
    answer = []
    for i in range(longest,prime_length):
        for j in range(i - longest, 0, -1):
            diff = primes_cum_sum_list[i] - primes_cum_sum_list[j]
            if diff <= limit:
                if prime_test(diff) and i - j > longest:
                    print diff
                    longest += 1
                    answer = [diff, longest]
            else:
                break
    return answer

start_time = time.time()
primes = sieve(1000000)
prime_sum = getPrimesCumSum(primes)
answer = findPrimeOfMostConsecutivePrimes(primes,prime_sum,25,1000000)
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. The answer is %s which is the sum of %s consecutive primes" % (run_time, answer[0], answer[1])



