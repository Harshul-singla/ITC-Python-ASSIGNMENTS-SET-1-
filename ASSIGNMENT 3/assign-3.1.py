'''
use re lib
for indexes of all repeting strings
re.finditer()
returns list of indexes
'''

str1 = input(">") 
#input string
str1 = " ".join(str1.split()) 
#used to remove duplicate spaces and whitespaces at the end

# tocount words in string with multiple words
if (' ' in str1):
    words = set(str1.split(' ')) #if ordered not arranged use list(dict.fromkeys(str1))
    for a in words: print(a, 'occurs', str1.count(a), 'times')

#count letters in a single word
else:
    for a in set(str1): print(a, 'occurs', str1.count(a), 'times')