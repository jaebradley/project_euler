"""
https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from utils.sieve_of_atkin import SieveOfAtkin
from utils.is_prime import is_prime


def return_all_concatenated_numbers(*numbers):
    concatenated_numbers = list()
    for number in numbers:
        other_numbers = list(numbers)
        other_numbers.remove(number)
        for other_number in other_numbers:
            concatenated_numbers.append(int(str(number) + str(other_number)))
            concatenated_numbers.append(int(str(other_number) + str(number)))
    return concatenated_numbers


sieve = SieveOfAtkin(limit=30000)
primes = sieve.getPrimes()
prime_length = len(primes)

for first_prime_index in range(1, prime_length):
    for second_prime_index in range(first_prime_index, prime_length):
        for third_prime_index in range(second_prime_index, prime_length):
            for fourth_prime_index in range(third_prime_index, prime_length):
                first_prime = primes[first_prime_index]
                second_prime = primes[second_prime_index]
                third_prime = primes[third_prime_index]
                fourth_prime = primes[fourth_prime_index]
                concatenated_numbers = return_all_concatenated_numbers(
                    first_prime,
                    second_prime,
                    third_prime,
                    fourth_prime
                )
                for concatenated_number in concatenated_numbers:
                    if not is_prime(number=concatenated_number):
                        break

                print first_prime, second_prime, third_prime, fourth_prime
