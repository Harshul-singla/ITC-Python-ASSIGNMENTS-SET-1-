#Qn1
inp = input('Enter String:') 
inp = " ".join(str1.split()) #remove extra spaces

# multiple words
if (' ' in inp):
    words = set(inp.split(' '))
    for b in words: print(b, ':', inp.count(b), 'times')

#count letters in a single word
else:
    for a in set(inp): 
        print(a, 'occurs', inp.count(a), 'times')

        
