'''
Find the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000
'''

def self_power(number):
    sum = 0
    for a in range(1,number + 1):
        sum += a ** a
    return sum

def last_digits(number,digits):
    string = str(number)
    length = len(string)
    end = length
    start = end - digits
    return string[start:end]

print last_digits(self_power(1000),10)