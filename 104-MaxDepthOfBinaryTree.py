# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:

    '''
    My solution
    DFS traversal (////////)
    O(n) time
    O(logn) memory for balanced tree, O(n) memory for worst case unbalanced
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if(root.left is None and root.right is None):
                return 1
            else:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0
