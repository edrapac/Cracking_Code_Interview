#sample input 5 4
# [1,2,3,4,5]
# 1 is [0] or [-5] becomes [1] or [-4] (0+-4)
# 2 is [1] becomes [1] or [-3]	(1 + -4)
# 3 is [2] becomes [2] or [-2]
# 4 is [3] becomes [3] or [-1]
# becomes [5,1,2,3,4]

def rotLeft(a,d):
	alist = []
	for i in range(a):
		alist.append(i)
	for i in range(len(alist)):
		newindex = (i-4)
		alist[i] , alist[newindex] = alist[newindex], alist[i]
	return alist
print(rotLeft(5,4))
