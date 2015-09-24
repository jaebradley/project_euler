def sum_div(x):
    div_sum = 0
    for div in range(1,x):
        if x % div == 0:
            div_sum += div
    return div_sum


amicable_sum=0
for a in range(2,10001):
    sum_a = sum_div(a)
    b = sum_a
    sum_b = sum_div(sum_div(a))
    if sum_b == a & a != b:
        print a,b
        amicable_sum += (a+b)/2
print amicable_sum
