
#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#column are set to 0.

#EDIT Wow that looks like shit but it works I guess....


matrix_1 = [  [4,5,6] ,  # Row 2 should be 0 as well as column 1 
			  [0,8,6] ,
			  [1,2,3] ]

def ZeroMatrix(matrix):
	zero_matrix = [   ['a','a','a'], ['a','a','a'] ,['a','a','a']  ]

	if len(matrix[0]) != len(matrix):
		print("Not an NxN Matrix please try again")
	

	else:
		for i in range(len(matrix)):
			for index,value in enumerate(matrix[i]):
				
				if value == 0:
					 
					matrix[i] = zero_matrix[i]
					for row in matrix:
						row[value] = 'a'
		
		for row in range(len(matrix)):
			for cell in range(len(matrix[0])):
				if matrix[row][cell] == 'a':
					matrix[row][cell] = 0
				
				
	return Matrix			
					

	


if __name__ == "__main__":
	ZeroMatrix(matrix_1)