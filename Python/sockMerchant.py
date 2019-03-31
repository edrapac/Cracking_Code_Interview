# if socklist = [1,2,1,2,1,3,2] then the max value is 2 because there are at most 2 pairs

def sockMerchant(socklist):
	socklist.sort()
	sockmap = {}
	pairs =0 
	for i in range(len(socklist)):
		sockmap[i] = 0
		for j in sockmap.keys():
			if socklist[i] == j:
				sockmap[j] +=1
	for i in sockmap.values():
		pairs += (i //2)
	return pairs
socklist = [1,2,1,2,1,3,2]
print(sockMerchant(socklist))