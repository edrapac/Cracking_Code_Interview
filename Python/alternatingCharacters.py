#You are given a string containing characters A  and B
#only.Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
#Your task is to find the minimum number of required deletions.
#AABAB = 1 Deletion
#AAAA = 3 Deletions
#AABBAB = 2 Deletions

def alternatingCharacters(astring):
	counter = 0
	for i in range(len(astring)-1):
		if astring[i] == astring[(i+1)]:
			counter +=1 
	return counter 


print(alternatingCharacters('AABAB'))
print(alternatingCharacters('AABBAB'))
print(alternatingCharacters('AAAA'))