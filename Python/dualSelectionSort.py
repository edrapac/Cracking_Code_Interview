
# Find the minimum and the maximum value in the list 
#(hint: you can keep track of both while doing a single loop)
# Swap the minimum value with the value in the first position.
# Swap the maximum value with the value in the last position.
# Repeat the steps above for the remainder of the list 
#(starting at the second position and ending at the second to last position 
#and narrowing the range of positions examined from both ends of the array each time).

def dualSelectionSort(unsortedlist):
	for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    j = 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
