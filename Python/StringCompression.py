# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def StringCompression(word):
	compressedString = "" #here we set the inital string to the first char of the word
	count =  1 #to count each time a char is encountered, must be reset a new char is encountered 
	current_char = word[0]
	for i in range(len(word) -1 ):
		if word[i] == word[i+1]:
			count+=1
			#current_char = str(word[i] + str(count))
			compressedString += current_char
		else:
			count = 1
			current_char = str(word[i] + str(count))
			compressedString += current_char
	return compressedString

if __name__ == '__main__':
	print(StringCompression('aabcccccaaa'))