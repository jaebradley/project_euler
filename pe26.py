'''
Find the value d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part

do the division, get the remainder
use the remainder, do the division, get the remainder
repeat
you can only know it's a cycle if you see the same pattern exactly twice where pattern length is <= d - 1
'''
recurring_list = list([0,0])
for a in range(2,1001):
    print a
    mod = 0
    rem = 1
    dig_list = list()
    while rem:
        rem = rem % a
        if rem in dig_list:
            if len(dig_list) - dig_list.index(rem) > recurring_list[1]:
                recurring_list = list([a,len(dig_list)])
            break
        dig_list.append(rem)
        rem *= 10

print recurring_list




