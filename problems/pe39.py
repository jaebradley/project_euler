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