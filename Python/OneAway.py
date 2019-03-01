#There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away
# pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bae -> false

#THIS COULD BE DONE WITH SWITCHES IN JAVA 


def OneAway(word1,word2):
	if ( (len(word1)-len(word2)) == 1 or (len(word1)-len(word2)) ==0 or (len(word1)-len(word2)) ==-1): #checks to see if we removed the proper 1 allowed char or didnt remove one, if we didnt remove one then we modified one 
		
		if ( (len(word1)-len(word2)) ==0 ):
			
			word1_chars = [chars for chars in word1]
			counter = 0
			for char in word2:
				if char not in word1:
					counter +=1
			if counter == 1:
				return True
			if counter > 1:
				return False
			else:
				print("zero edits")

		if ( (len(word1)-len(word2)) == 1 or (len(word1)-len(word2)) ==-1):
			count =0
			word1_chars = [chars for chars in word2]
			for char in word1:
				if char not in word2:
					count+=1
			if count>1:
				return False
			else:
				return True 




	else: #too many chars removed 
		return False


if __name__ == '__main__':
	val1 = OneAway('pale','ple')
	val2 = OneAway('pale','pales') 
	val3 = OneAway('pale','bae') 
	val4 = OneAway('pale','pale')
	if(val1):
		print('True')

	if(val2):
		print('True')

	if(val3):
		print('True')
	else:
		print('False')

	if(val4):
		print('True')