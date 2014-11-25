import string
alphabet_value = dict(zip(string.ascii_uppercase, range(1,27))) #get a dictionary of letters and alphabetic-rank values
file = open('pe22_names.txt').read().split(',') #read list of names
file.sort() #sort alphabetically
name = ''
score = 0
final_score = 0
for i in range(0,len(file)): #for every name in file, get it's rank (by iterating by 1 in score variable)
    name = file[i].strip('"')
    score += 1
    subscore = 0
    for j in range(0, len(name)): #for each name, iterate through each letter and get it's alphabet score (subscore)
        l = name[j]
        print l
        val = alphabet_value[l]
        subscore += val
    final_score += score * subscore #add the product of rank score and alphabet score to the final score
print final_score