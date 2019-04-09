
'''shared_ancestor(four, one, six) is four
shared_ancestor(four, three, seven) is four
shared_ancestor(four, two, four) is four
shared_ancestor(four, one, three) is two
shared_ancestor(four, five, six) is six'''

class BNode:
    '''Node for a simple binary tree structure'''
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
def shared_ancestor(root, node1, node2):
    '''Given the root of a binary tree, and two nodes in that tree, 
    return the lowest shared ancestor of the two nodes'''
    if node1.value > node2.value: # keeps track of which one is the largest
        maxval = node1
        lowval = node2
    else:
        maxval = node2
        lowval = node1
    rootleft = root.left
    
    if node1.value == root.value or node2.value==root.value: #if either is the root value
        return root
    
    if (maxval.value - lowval.value) == 1: #if there is a difference of 1 between the 2 children nodes
        return maxval
    
    if (maxval.value < root.value) and ((maxval.value - root.value)==1): # if we have a difference of 1 with the max val
        return rootleft
    if (lowval.value > root.value) and ((lowval.value-root.value)==1):
        return maxval
    if (maxval.value - lowval.value) > 1:
        return root



one= BNode(1,None,None)
three = BNode(3,None,None)
two = BNode(2,one,three)
four = BNode(4,two,None)

print(shared_ancestor(four,one,three).value)