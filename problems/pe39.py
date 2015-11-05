"""
If p is the perimeter of a right triangle, which value for p <= 1000 has the most solutions?
"""
import math

count_dict = {}
for x in range(0,1001):
    count_dict[x] = 0

print count_dict[12.0]
count = 0
p = 1000
for a in range(1,p - 1):
    count = 0
    print a
    for b in range(1,p - 1):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c <= 1000 and c.is_integer() == 1:
            sum = int(a + b + c)
            count_dict[sum] += 1

""" a) create a list of the dict's keys and values;
         b) return the key with the max value"""

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

key = keywithmaxval(count_dict)
print key,count_dict[key]

def return_pythagorean_triplets_which_sum_under_limit(limit):
    pythagorean_triplets = list()
    side_length_limit = int(math.floor(limit / 2))
    for a in range(1, side_length_limit):
        for b in range(a + 1, side_length_limit):
            hypotenuse_squared = a ** 2 + b ** 2
            # TODO: come up with a better integer identifier
            if int(hypotenuse_squared) == hypotenuse_squared:
                hypotenuse = math.sqrt(hypotenuse_squared)
                if int(hypotenuse) == hypotenuse and a + b + hypotenuse <= limit:
                    pythagorean_triplets.append(a + b + hypotenuse)
    return pythagorean_triplets

print return_pythagorean_triplets_which_sum_under_limit(1000)