class Node:
    """Simple node for singly-linked list"""
    def __init__(self, value, next=None):
        """Create a new node, with optional next node pointer"""
        self.value = value
        self.next = next

def stalin_sort(l):
    nearpointer = l
    farpointer = l.next
    
    

    while farpointer != None: # if there is more than one element in the list
        if nearpointer.value > farpointer.value: # if the current element is greater than the next
            farpointer = farpointer.next
        elif farpointer.value >= nearpointer.value:
                nearpointer = farpointer
                farpointer = farpointer.next

    return l.value

node3 = Node(value = '20', next = None)
node2 = Node(value = '10',next=node3)
node1 = Node(value = '30',next=node2)


print(stalin_sort(node1))