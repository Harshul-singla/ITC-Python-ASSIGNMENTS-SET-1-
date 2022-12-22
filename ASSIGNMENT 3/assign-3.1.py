#Qn1
inp = input(">") 
inp = " ".join(str1.split()) #remove extra spaces

# multiple words
if (' ' in inp):
    words = set(inp.split(' '))
    for a in words: print(a, 'occurs', inp.count(a), 'times')

#count letters in a single word
else:
    for a in set(inp): 
        print(a, 'occurs', inp.count(a), 'times')
