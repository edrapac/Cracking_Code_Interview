# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
#Could you do it without extra space and in O(n) runtime?
# to do this in O(n) we need to iterate over the entire list only once 
# to do this without extra space, we cannot create another list
list1 = [1,3,3,4,4,5,5]
# [3,3,4,4,5] i =0
#[3,4,4,5] i =1
#[3,4,5] i=2
def findDuplicates(alist):
	alist.sort()
	newlist = []
	i = 0
	while (i < (len(alist)-1)):
		if alist[i] == alist[(i+1)]: #if we found a duplicate value
			newlist.append(alist[(i+1)])
			i+=1
		else: # not a duplucate, remove it
			print(i)
			alist.pop(i)
			
	return newlist

print(findDuplicates(list1))