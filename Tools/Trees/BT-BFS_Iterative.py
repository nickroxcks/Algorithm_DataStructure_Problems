'''
For BFS (Level Order Traversal), we use a Que for the iterative approach

Time Complexity: O(N) where N is the number of nodes in the binary tree.
Auxiliary Space: O(N) where N is the number of nodes in the binary tree.

Extra Space required for Level Order Traversal is O(w) where w is maximum width of Binary Tree.


We need to visit the nodes in a lower level before any node in a higher level,
this idea is quite similar to that of a queue. Push the nodes of a lower level in the queue.
When any node is visited, pop that node from the queue and push the child of that node in the queue.
This ensures that the node of a lower level are visited prior to any node of a higher level.

'''
# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver Program to test above function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level Order Traversal of binary tree is -")
    printLevelOrder(root)