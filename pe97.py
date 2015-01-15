# coding=utf-8
__author__ = 'jaebradley'
'''
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
'''

import project_euler_helpers as pe
import time
'''
2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048
'''
start_time = time.time()
number = 28433 * pow(2,7830457,10000000000) + 1
digits = pe.getDigits(int(number))
last_digits = '' . join(str(digit) for digit in digits[len(digits)-10:])
answer = last_digits
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s" % (run_time, answer)