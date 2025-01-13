'''
DFS Iterative Approaches

DFS Iterative Preorder using Morris Traversal:
Time Complexity: O(n), we visit every node at most once.
Auxiliary Space: O(1), we use a constant amount of space for variables and pointers.
Limitations:
Morris’s traversal modifies the tree during the process. It establishes the right links while moving down the tree
and resets the right links while moving up the tree.
So the algorithm cannot be applied if write operations are not allowed.

DFS Iterative Preorder Traversal no Morris using stack:
Time Complexity: O(N)
Auxiliary Space: O(H), where H is the height of the tree.

DFS Iterative Postorder Traversal
Time complexity: O(n) where n is no of nodes in a binary tree
Auxiliary space: O(n) because using stack s1 and s2


'''

# A binary tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
Using Morris Traversal, we can traverse the tree without using stack and recursion. 
The algorithm for Preorder is almost similar to Morris traversal for Inorder.

1...If left child is null, print the current node data. Move to right child. 
….Else, Make the right child of the inorder predecessor point to the current node. Two cases arise: 
………a) The right child of the inorder predecessor already points to the current node. Set right child to NULL. Move to right child of current node. 
………b) The right child is NULL. Set it to the current node. Print the current node’s data and move to left child of current node. 
2...Iterate until the current node is not NULL.
'''
# Preorder traversal without
# recursion and without stack
def MorrisTraversal(root):
    curr = root

    while curr:
        # If left child is null, print the
        # current node data. And, update
        # the current pointer to right child.
        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right

        else:
            # Find the inorder predecessor
            prev = curr.left

            while prev.right is not None and prev.right is not curr:
                prev = prev.right

                # If the right child of inorder
            # predecessor already points to
            # the current node, update the
            # current with it's right child
            if prev.right is curr:
                prev.right = None
                curr = curr.right

                # else If right child doesn't point
            # to the current node, then print this
            # node's data and update the right child
            # pointer with the current node and update
            # the current with it's left child
            else:
                print(curr.data, end=" ")
                prev.right = curr
                curr = curr.left

# Function for Standard preorder traversal
def preorfer(root):
    if root:
        print(root.data, end=" ")
        preorfer(root.left)
        preorfer(root.right)


''' Iterative Preorder traversal no Morris
    Following is a simple stack based iterative process to print Preorder traversal. 

        1)Create an empty stack nodeStack and push root node to stack. 
        2)Do the following while nodeStack is not empty. 
            1)Pop an item from the stack and print it. 
            2)Push right child of a popped item to stack 
            3)Push left child of a popped item to stack

    The right child is pushed before the left child to make sure that the left subtree is processed first.

'''
def iterativePreorder(root):
    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while (len(nodeStack) > 0):

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.data, end=" ")

        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

'''
DFS Iterative Postorder Traversal
Time complexity: O(n) where n is no of nodes in a binary tree
Auxiliary space: O(n) because using stack s1 and s2
'''
# An iterative function to do postorder
# traversal of a given binary tree
def postOrderIterative(root):
    if root is None:
        return

        # Create two stacks
    s1 = []
    s2 = []

    # Push root to first stack
    s1.append(root)

    # Run while first stack is not empty
    while s1:

        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)

        # Push left and right children of
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

            # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.data, end=" ")
    # Driver program to test Morris
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)

root.left.right.left = Node(10)
root.left.right.right = Node(11)

MorrisTraversal(root)
print("\n")
preorfer(root)

# Driver program to test iterative preorder
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
iterativePreorder(root)

# Driver program to test post order
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrderIterative(root)