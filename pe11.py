import csv
import time

start = time.time()
num_file = open('/Users/jaebradley/Desktop/euler_11.csv','r')
num_list = list(csv.reader(num_file))
max_prod = 0
for i in range(20):
    for j in range(16):
        # right/left products
        prod = int(num_list[i][j])*int(num_list[i][j+1])*int(num_list[i][j+2])*int(num_list[i][j+3])
        if prod > max_prod: max_prod = prod
        # up/down products
        prod = int(num_list[j][i])*int(num_list[j+1][i])*int(num_list[j+2][i])*int(num_list[j+3][i])
        if prod > max_prod: max_prod = prod

# diagonal products
for i in range(16):
    for j in range(16):
        prod = int(num_list[i][j])*int(num_list[i+1][j+1])*int(num_list[i+2][j+2])*int(num_list[i+3][j+3])
        if prod > max_prod: max_prod = prod
for i in range(3,20):
    for j in range(16):
        prod = int(num_list[i][j])*int(num_list[i-1][j+1])*int(num_list[i-2][j+2])*int(num_list[i-3][j+3])
        if prod > max_prod: max_prod = prod

elapsed = (time.time() - start)

print "%s found in %s seconds" % (max_prod,elapsed)
