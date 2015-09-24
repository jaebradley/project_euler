import math
sum = 0
num = '{0:f}'.format(math.pow(2,1000)).rstrip('0').rstrip('.') #get 2^1000, strip 0s after decimal point and then decimal point because python formatting sucks

for x in range(0,len(num)):
    sum = sum + int(num[x]) #for each digit in number, sum the digits
print sum