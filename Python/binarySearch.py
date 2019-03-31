#must be a sorted list.
#given a sorted list what is a good way to find the particular index of a number? Binary search

def binarySearch(searchnumber,alist):
	first = 0
	last = (len(alist) -1)
	midpoint = len(alist) // 2
	found = False

	while not found:
		if alist[midpoint] > searchnumber:
			last = midpoint
			midpoint = ((last - first) //2)

		if alist[midpoint] < searchnumber:
			first = midpoint
			midpoint = ((last - first) //2)

		if alist[midpoint] == searchnumber:
			found = True
	return midpoint

list1 = [1,2,3,4,5,6,7,8,9,10]

print(binarySearch(3,list1))