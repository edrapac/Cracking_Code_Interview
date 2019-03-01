#input aba 10
# output = 7 (abaabaabaa) =  7 a's
astring = 'aba'

def repeatedString(astring,length):
	multtime = (length // len(astring))+1
	repeatedstring = astring*multtime
	counter = 0
	for i in range(0,length):
		if repeatedstring[i] == 'a':
			counter+=1
	return counter 
print(repeatedString(astring,10))