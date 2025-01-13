from typing import Optional


class Node:

    def __init__(self):
        self.key = 0
        self.left, self.right = None, None
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def newNode(key):
    temp = Node()
    temp.key = key
    temp.left, temp.right = None, None
    return temp

'''
Find height of tree using DFS
O(n) time, O(logn) memory for balanced tree, O(n) memory worst case unbalanced tree

The solution is simply finding the heights of the left and right sub trees, 
taking the max of them, and then adding 1

See leetcode problem #104 and in written notes
'''
# Function to find the height(depth) of the tree
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root:
        if (root.left is None and root.right is None):
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    else:
        return 0