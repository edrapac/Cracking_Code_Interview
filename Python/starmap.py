import heapq
class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    
    @property
    def distance(self):
        return self.x**2 + self.y**2 + self.z**2 
    
def k_closest_stars(k, stars):

    the_heap = []
    i = 0 
    heapq.heapify(the_heap)
    heap_dict = {}

    for arrays in stars: '''FIX ME PLZ'''
        newstar = Star(arrays[0],arrays[1],arrays[2])
        heap_dict[newstar.distance] = i
        i+=1
	
        heapq.heappush(the_heap,newstar.distance)
    allist = heapq.nsmallest(k,the_heap)
    smallist = []
    for i in range(len(allist)):
    	smallist.append(heap_dict[allist[i]])
    	
    
    return smallist