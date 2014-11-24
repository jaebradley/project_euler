file = open('pe.txt') #open file with the one hundred 50-digit numbers
output = file.read() #read from file
output_list = output.split() #string output to list
output_list = map(int,output_list) #list elements are string -- convert to integers
sum = sum(output_list) #find the sum of all the list elements
str_sum = str(sum) #convert to string to get the first 10 digits of sum
print str_sum[0:10] #get first 10 digits of sum