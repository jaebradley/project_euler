__author__ = 'jaebradley'
#find all the distinct combinations of a^b where a and b are between 2 and 100 inclusive
numbers=[];

for a in range(2,101):
    for b in range(2,101):
        numbers.append(a**b);

distinct_numbers = set(numbers);
print len(distinct_numbers);