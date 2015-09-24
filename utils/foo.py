__author__ = 'jaebradley'
import math;

def dig_count(num):
    digits = int(math.log10(num))+1; #calculate the digits of a number
    return digits;

def fib(dig):
    data=[1,1]; #store initial fibonacci numbers
    ans=2; #set some arbitrary non-zero value for ans
    while dig_count(ans) < dig: #while digit count is greater than the digit count specified calculate next fibonacci number and then store
        n=len(data);
        ans=data[n-1] + data[n-2];
        data.append(ans); #store fibonacci number
    return data[n];

print fib(1000);
