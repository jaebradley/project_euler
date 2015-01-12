__author__ = 'jaebradley'
'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Brute Force Strategy:

1.  Iterate through all numbers
    (thought about instituting restriction that x must start with 1
    but I believe there are some corner cases where this doesn't work)
2.  Get all digits for each number as a list
3.  For a multiplier from 1 to 6, if the sorted digits of the product are the same
    as the sorted digits from the original number then "success" variable is 1, else it is 0
    and the inner for loop breaks in order to move on to the next number
4.  If success variable = 1 then assign i to answer variable and break outer for loop
    to stop iterating through numbers
'''

import time
import project_euler_helpers as pe

start_time = time.time()
answer = 0
for i in range(1,10000000):
    same_digits = 0
    digit_list = pe.getDigits(i)
    for j in range(1,7):
        if sorted(pe.getDigits(i * j)) != sorted(digit_list):
            same_digits = 0
            break
        else:
            same_digits = 1
    if same_digits == 1:
        answer = i
        break

end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s." % (run_time, answer)