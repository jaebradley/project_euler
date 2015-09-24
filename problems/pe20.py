__author__ = 'jaebradley'
# find the sum of the digits for 100!

import math;
digit = math.factorial(100) ;
num = 0;
for i in str(digit):
    num += int(i);

print num; # answer is 648