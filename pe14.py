

def collatz(n):
    if n % 2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
    return n

def long_chain(n):
    count_list = list()
    for i in range(1,n + 1):
        count = 0
        num = i
        while num > 1:
            num = collatz(num)
            count = count + 1
        count = count + 1
        count_list.append(count)
    return max(count_list)

print long_chain(1000000)