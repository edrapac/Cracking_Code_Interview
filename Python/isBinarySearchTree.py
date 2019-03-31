#Implement the function isBinarySearchTree(root), which returns True if the binary tree passed to it is a valid binary search tree.
#examples:
# root0 = TreeNode(10, TreeNode(5, None, None), TreeNode(15, None, None))
# isBinarySearchTree(root0) == True
# root1 = TreeNode(20, TreeNode(5, None, None), TreeNode(15, None, None))
# isBinarySearchTree(root1) == False
# root2 = TreeNode(20, TreeNode(10, None, TreeNode(25, None, None)), TreeNode(30, None, None))
# isBinarySearchTree(root2) == False
# root3 = TreeNode(10, TreeNode(5, None, None), None)
# isBinarySearchTree(root3) == True
# root4 = TreeNode(10, None, TreeNode(15, None, None))
# isBinarySearchTree(root4) == True



class TreeNode:
    '''Node for a simple binary tree structure'''
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def isBinarySearchTree(tree):
	flag = True
	leftcurrent = tree #we will traverse the tree seperately and merge results at the end
	rightcurrent = tree # 'currents' work as pointers to current node
	
	while (leftcurrent): # allows us to iterate over a tree,once we reach the end this loop stops, this branch is for the left side of the tree
		if (leftcurrent.left.value): #if the node has a left node
			if (leftcurrent.value > leftcurrent.left.value): # if the parent node is greater than it's left child
				leftcurrent = leftcurrent.left #advance current node pointer to next node
			else:
				flag = False # if left child is greater than parent return false

	#traverse right side of tree
	while (rightcurrent):
		if (rightcurrent.right.value): #if the parent node has a right child node
			if (rightcurrent.value < rightcurrent.right.value): #if the right child node is greater than the parent node
				rightcurrent = rightcurrent.right #advance current node pointer to next node
			else:
				flag = False

	return flag

if __name__ == '__main__':
	root0 = TreeNode(10, TreeNode(5, None, None), TreeNode(15, None, None))
	print(isBinarySearchTree(root0))