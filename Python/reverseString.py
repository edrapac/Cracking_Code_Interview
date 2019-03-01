
def reverseString(astring):
	newstring = ''
	astring = list(astring)
	index = len(astring)
	while index>0:
		index -= 1
		newstring += astring[index]
	return newstring
print(reverseString('hennaj'))
print(reverseString('reverse'))