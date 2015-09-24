from utils import project_euler_helpers as pe

__author__ = 'jaebradley'
'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

import time
start_time = time.time()
max_digit_sum = 0

for a in range(1,100):
    for b in range(1,100):
        number = a ** b
        digits = pe.getDigits(number)
        digit_sum = sum(digits)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
answer = max_digit_sum
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s" % (run_time,answer)
