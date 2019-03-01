
def URLify(word):
	space_char = '%20'
	print(dir(word))
	word2 = word.replace(" ",'%20')
	print(word2)

if __name__ == '__main__':
	URLify("John Smith")