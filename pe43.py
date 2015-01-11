__author__ = 'jaebradley'
'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Solved this last because it took me the longest to solve.

Brute Force Strategy:

1. Generate all pandigital numbers by string concatentating 10 distinct digits (non-trivial for me)
    a. Using list comprehension one can iterate over 10 different digits and exclude any previously selected digits
2. Check if the different digit combinations are divisible by the given numbers
3. If they are, then append the pandigital number to the pandigital list
'''

import time

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
                                            combination1 = int(str(num2) + str(num3) + str(num4))
                                            combination2 = int(str(num3) + str(num4) + str(num5))
                                            combination3 = int(str(num4) + str(num5) + str(num6))
                                            combination4 = int(str(num5) + str(num6) + str(num7))
                                            combination5 = int(str(num6) + str(num7) + str(num8))
                                            combination6 = int(str(num7) + str(num8) + str(num9))
                                            combination7 = int(str(num8) + str(num9) + str(num10))
                                            if combination1 % 2 == 0 and combination2 % 3 == 0 and combination3 % 5 == 0 and combination4 % 7 == 0 and combination5 % 11 == 0 and combination6 % 13 == 0 and combination7 % 17 == 0:
                                                print pandigital
                                                pandigital_list.append(pandigital)
    return pandigital_list

start_time = time.time()
pandigital_list = getPandigitals()
answer = sum(pandigital_list)
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s and the pandigital list is %s" % (run_time, answer, pandigital_list)
