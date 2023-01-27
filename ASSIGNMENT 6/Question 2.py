def Palin(phr):	
	l1 = list(''.join(phr.split()))
	if l1 == list(reversed(l1)):	
     
		return True 
	else:
		return False
	
	
	
inp = input('Enter a Phrase: ')
if Palin(inp):
	print("Tis a palindrome. ")
	
else: 
	print('Tis not.')