import datetime #pretty much cheating here, but whatever
count = 0
for month in range(1,13):
    for year in range(1901,2001):
        if(datetime.datetime.strptime(str(month) + '/01/' + str(year), '%m/%d/%Y').strftime('%A')) == 'Sunday':
            count += 1 #add to count if day equals Sunday
print count