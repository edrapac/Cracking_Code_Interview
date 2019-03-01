def isUnique(word):
	full_word = [letter for letter in word]
	char_list = []
	for letter in word:
		letter = letter.lower()
		if letter not in char_list:
			char_list.append(letter)
	if (len(full_word) == len(char_list)):
		print('Word contains all unique Chars')
	else:
		print('Word did not contain all unique chars')




if __name__ == '__main__':
	isUnique('Test')
	isUnique('Tes')