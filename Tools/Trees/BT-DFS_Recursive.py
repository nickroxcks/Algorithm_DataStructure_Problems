'''
For DFS, there are 3 different traversal methods that can be used in dfs
-inorder O(N) time O(logN) memory
-preorder O(N) time O(logN) memory
-post order O(N) time O(logN) memory

DFS is typcially recursive


It is evident from above points that extra space required for Level order traversal is likely to be more when
tree is more balanced and extra space for Depth First Traversal is likely to be more when tree is less balanced.

How to Pick One DFS of BFS?
1)Extra Space can be one factor (Explained above)
2)Depth First Traversals are typically recursive and recursive code requires function call overheads.
3)The most important points is, BFS starts visiting nodes from root while DFS starts visiting nodes from leaves.
So if our problem is to search something that is more likely to closer to root, we would prefer BFS.
And if the target node is close to a leaf, we would prefer DFS
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
'''
            1
           /\ 
          2  3
         /\
        4  5 
Inorder Recursive O(N) time O(logN) memory (aka O(h) memory)
    1)Traverse the left subtree, i.e., call Inorder(left-subtree)
    2)Visit the root
    3)Traverse the right subtree, i.e., call Inorder(right-subtree)
[4 2 5 1 3]
In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
To get nodes of BST in non-increasing order, a variation of Inorder traversal 
where Inorder traversal is reversed can be used
'''
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


'''
            1
           /\ 
          2  3
         /\
        4  5 
Postorder Recursive O(N) time O(logN) memory (aka O(h) memory)
    
    1)Traverse the left subtree, i.e., call Postorder(left-subtree)
    2)Traverse the right subtree, i.e., call Postorder(right-subtree)
    3)Visit the root

[4 5 2 3 1]
Postorder traversal is used to delete the tree. Please see the question for the deletion of the tree for details. 
Postorder traversal is also useful to get the postfix expression of an expression tree
'''
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),



'''
            1
           /\ 
          2  3
         /\
        4  5 
Preorder Recursive O(N) time O(logN) memory (aka O(h) memory)
    1)Visit the root
    2)Traverse the left subtree, i.e., call Preorder(left-subtree)
    3)Traverse the right subtree, i.e., call Preorder(right-subtree)
[1 2 4 5 3]
Preorder traversal is used to create a copy of the tree. 
Preorder traversal is also used to get prefix expressions of an expression tree.     
'''
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val)

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)
