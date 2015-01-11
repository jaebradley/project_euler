__author__ = 'jaebradley'

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

BRUTE FORCE STRATEGY:

1. Get all 4 digit primes
2. Get the digits of these primes and create a dictionary keyed on
   the sorted tuple of their digits with the value associated with each key
   being all primes that share the same digit
3. In this way, the dictionary tracks all the primes that are permutations of each other via their sorted digits
4. From this dictionary, get each key with at least 3 primes associated with it
   and create all possible 3 prime triplets. Store triplets in list.
5. Run through the list and find the diff amongst the first and second values in the triplet and the second and third values in the triplet.
   If the diffs are the same then the sequence is arithmetic.
'''

import time
import numpy

def getDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return tuple(sorted(digit_list)),digit_list

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

def getPrimePermutationDictionary(primes_list):
    prime_dict = {}
    for prime in primes_list:
        digit_data = getDigits(prime)
        digit_tuple = digit_data[0]
        digit_list = digit_data[1]
        if len(digit_list) == 4:
            if digit_tuple in prime_dict:
                prime_dict[digit_tuple]['primes'].append(prime)
            else:
                prime_dict[digit_tuple] = {
                    'primes':[prime]
                }
    return prime_dict

def getAllPrimeCombinations(prime_permutation_dictionary):
    prime_triplets_list = []
    for key in prime_permutation_dictionary:
        prime_list = prime_permutation_dictionary[key]['primes']
        if len(prime_list) >= 3:
            for i in range(0,len(prime_list)):
                for j in range(i,len(prime_list)):
                    for k in range(j,len(prime_list)):
                        num1 = prime_list[i]
                        num2 = prime_list[j]
                        num3 = prime_list[k]
                        if num1 != num2 and num1 != num3 and num2 != num3:
                            prime_triplets_list.append(sorted([num1, num2, num3]))
    return prime_triplets_list

def findArithmeticTriplet(prime_triplets_list):
    answer_list = []
    for triplet in prime_triplets_list:
        diff1 = triplet[1] - triplet[0]
        diff2 = triplet[2] - triplet[1]
        if diff1 == diff2:
            answer_list.append(str(triplet[0]) + str(triplet[1]) + str(triplet[2]))
    return answer_list

start_time = time.time()
primes = sieve(9999)
prime_permutations = getPrimePermutationDictionary(primes)
prime_triplets = getAllPrimeCombinations(prime_permutations)
answer = findArithmeticTriplet(prime_triplets)
end_time = time.time()
run_time = end_time - start_time
print "Finished in %s seconds. Answer list: %s" % (run_time, answer)



