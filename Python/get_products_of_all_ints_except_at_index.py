#   [1, 7, 3, 4]
#   [84, 12, 28, 21]
# [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
# cant use division in the final answer
# so [1*2*3,0*2*3,0*1*3,0*1*2]

def get_products_of_all_ints_except_at_index(alist):
	newlist = []
	newnum = 1
	for i in range(len(alist)):
		skipindex = i

		for j in range(len(alist)):
			if j != i:
				newnum = newnum*(alist(j))
		newlist.append()