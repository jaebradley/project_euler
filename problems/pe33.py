__author__ = 'jaebradley'
num_log = []

for z in range(11,100):
    for i in range(10,100):
            str_i = str(i)
            str_z = str(z)
            x0 = float(str_i[0])
            x1 = float(str_i[1])
            x2 = float(str_z[0])
            x3 = float(str_z[1])
            num = float(i)/float(z)
            if x0 != 0.0 and x1 != 0.0 and x2 != 0.0 and x3 != 0.0:
                if x0 == x2 and x1/x3 < 1 and x1/x3 == num:
                    num_log.append([i,z])
                elif x0 == x3 and x1/x2 < 1 and x1/x2 == num:
                    num_log.append([i,z])
                elif x1 == x2 and x0/x3 < 1 and x0/x3 == num:
                    num_log.append([i,z])
                elif x1 == x3 and x0/x2 < 1 and x0/x2 == num:
                    num_log.append([i,z])

print num_log