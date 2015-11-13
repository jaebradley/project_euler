from utils.sieve_of_atkin import SieveOfAtkin
import time


def is_palindrome(alphanumeric):
    alphanumeric_string = str(alphanumeric)
    alphanumeric_string_length = alphanumeric_string.__len__()
    for start_position in range(0, alphanumeric_string_length):
        end_position = alphanumeric_string_length - 1 - start_position  # string is zero indexed but string length is one indexed
        if end_position < start_position:
            return True
        else:
            if alphanumeric_string[start_position] != alphanumeric_string[end_position]:
                return False


def return_distinct_prime_factors(number):
    prime_factors = []
    candidate_divisor = 2
    while candidate_divisor*candidate_divisor <= number:
        while 0 == (number % candidate_divisor):
            prime_factors.append(candidate_divisor)  # supposing you want multiple factors repeated
            number /= candidate_divisor
        candidate_divisor += 1
    if number > 1:
       prime_factors.append(number)
    return set(prime_factors)
