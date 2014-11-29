__author__ = 'jaebradley'

def translate(string):
    new_string=""
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(string)):
        new_letter=""
        if string[i] not in alpha:
            new_letter=string[i]
        else:
            num=alpha.index(string[i])
            if num>=24:
                new_letter=alpha[(num+1)%25]
            elif num==23:
                new_letter=alpha[25]
            else:
                new_letter=alpha[(num+2)%25]
        new_string+=new_letter
    print new_string

translate("http://www.pythonchallenge.com/pc/def/map.html")




