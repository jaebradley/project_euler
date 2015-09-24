import math

def tri_num(n):
    #get nth triangular number
    return n*(n+1)/2

def num_divisors(x):
    #count of divisors -- only need to count divisors until sqrt(x) and then multiply by 2 unless sqrt(x) is an integer, then add 1
    count = 0
    for i in range(1,math.trunc(math.sqrt(x))):
        #for divisor from 1 to integer less than sqrt(x)
        if (x/float(i)).is_integer():
            #if division results in integer then add to count
            count = count + 2
    if(math.sqrt(x) % 10).is_integer():
        #if sqrt(x) is an integer, add 1
        count = count + 1
    return count

def first_tri_num_with_p_divisors(p):
    div = 0
    n = 0
    num = 0
    while div <= p:
        num = tri_num(n)
        div = num_divisors(num)
        n = n + 1
        print div, num
    return num

print first_tri_num_with_p_divisors(501)
