__author__ = 'jaebradley'
import urllib2
from collections import defaultdict
response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
page_source = response.read()
start = page_source.find("<!--\n%")
end = page_source.find("*\n-->")
string = page_source[start+7:end]

'''
d = defaultdict(int)
for i in string:
    d[i] += 1
for letter,count in d.iteritems():
    print letter,count
'''
alpha="abcdefghijklmnopqrstuvwxyz"
message=""
for i in string:
    if i in alpha:
        message += i

print message
