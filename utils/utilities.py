import numpy


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


def is_triangular(number):
    """
    inverse function for triangular number
    :param number:
    :return:
    """
    return not (-1 + (1 + 8 * number) ** 0.5)/2 % 1


def is_pentagonal(number):
    """
    inverse function for pentagonal number
    :param number:
    :return:
    """
    return not (1 + (1 + 24 * number) ** 0.5)/6 % 1


def get_digits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return digit_list


def is_pandigital(candidate_number):
    digits = get_digits(candidate_number)
    if (max(digits) != len(digits)) or (min(digits) != 1):
        return False

    if len(set(digits)) != len(digits):
        return False

    for required_digit in range(1, len(digits) + 1):
        if required_digit not in digits:
            return False

    return True


# from http://stackoverflow.com/a/1801446
def is_prime(number):
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= number:
        if number % i == 0:
            return False

        i += w
        w = 6 - w

    return True


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
