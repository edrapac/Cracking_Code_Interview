

'''shared_ancestor(four, one, six) is four
shared_ancestor(four, three, seven) is four
shared_ancestor(four, two, four) is four
shared_ancestor(four, one, three) is two
shared_ancestor(four, five, six) is six'''
'''root is 8 node1 is 10 node2 is 15'''
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
    # print(maxval.value)
    # print(root.value)
    # print(lowval.value)
    rootleft = root.left
    
    if maxval.value == root.value or lowval.value==root.value: #if either is the root value
        return root
    
    if (maxval.value - lowval.value) == 1: #if there is a difference of 1 between the 2 children nodes ie one is the parent
        return maxval
    
    if (maxval.value < root.value) and ((maxval.value - root.value)==-1): # if we have a difference of 1 with the max val, ie both nodes are children of rootleft
        return rootleft
    
    if (lowval.value > root.value) and ((lowval.value-root.value)==1): #if the lowval is higher up the tree
        return maxval
        
    if (maxval.value - lowval.value) > 1: #if both children are at different levels
        return root
    



one= BNode(1,None,None)
three = BNode(3,None,None)
two = BNode(2,one,three)
four = BNode(4,two,None)

print(shared_ancestor(four,one,three).value)