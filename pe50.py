'''
NOT COMPLETE
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

prime_list = sieve(1000)
consecutive = 15
start_pos = 0
end_pos = start_pos + consecutive
consecutive_prime_list = prime_list[start_pos:end_pos]
result_list = list([0,2])

for a in range(0,len(prime_list)):
    start_pos = a
    end_pos = start_pos + consecutive
    if end_pos > len(prime_list) - 1:
        break
    old_consecutive = consecutive
    new_consecutive = consecutive
    consecutive_prime_list = prime_list[start_pos:end_pos]
        if is_prime(sum(consecutive_prime_list)):
            print old_consecutive
            consecutive = old_consecutive
            new_consecutive += 1
            end_pos = start_pos + new_consecutive
            consecutive_prime_list = prime_list[start_pos:end_pos]
        else:
            break




