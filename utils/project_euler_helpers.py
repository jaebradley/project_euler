__author__ = 'jaebradley'

import math
import numpy

def getDigits(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return digit_list

def isPandigital(number):
    digit_list = getDigits(number)
    if (max(digit_list) != 9) or (min(digit_list) != 1):
        return 0
    else:
        for i in range(1,len(digit_list) + 1):
            try:
                digit_list.remove(i)
            except ValueError:
                return 0
        if not digit_list:
            return 1
        else:
            return 0

def getPandigitals():
    pandigital_list =[]
    digits = [0,1,2,3,4,5,6,7,8,9]
    for num1 in digits:
        print num1
        for num2 in [num for num in digits if num != num1]:
            for num3 in [num for num in digits if num not in [num1,num2]]:
                for num4 in [num for num in digits if num not in [num1,num2,num3]]:
                    for num5 in [num for num in digits if num not in [num1,num2,num3,num4]]:
                        for num6 in [num for num in digits if num not in [num1,num2,num3,num4,num5]]:
                            for num7 in [num for num in digits if num not in [num1,num2,num3,num4,num5,num6]]:
                                for num8 in [num for num in digits if num not in [num1,num2,num3,num4,num5,num6,num7]]:
                                    for num9 in [num for num in digits if num not in [num1,num2,num3,num4,num5,num6,num7,num8]]:
                                        for num10 in [num for num in digits if num not in [num1,num2,num3,num4,num5,num6,num7,num8,num9]]:
                                            pandigital = int(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num8) + str(num9) + str(num10))
                                            pandigital_list.append(pandigital)
    return pandigital_list


def prime_test(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

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

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def reverse_string(string):
    return str(string)[::-1]