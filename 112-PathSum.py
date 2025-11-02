'''
LeetCode 112 Easy - Path Sum

My solution:
O(n) time for full scan of tree worst case
O(n) memory for worst case storing full tree in stack memory

- Utilize DFS traversal since we care about reaching leafs quickly
- For each node visit, also track the current sum at the point
- Accomplish this by adding additional field to TreeNode object
- For each node during DFS traversal:
    - If the sum equals the target sum when the node is popped, return True
    - Add the left/right children and their corresponding sums
If the loop finishes and no targetSum is found, return False
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, treeSum=None):
        self.val = val
        self.left = left
        self.right = right
        self.treeSum = TreeSum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base Case
        if root is None:
            return False

        root.treeSum = root.val

        # create an empty stack and push root to it
        nodeStack = []
        nodeStack.append(root)

        # Pop all items one by one. Do following for every popped item
        # a) push its right child
        # b) push its left child
        # Note that right child is pushed first so that left
        # is processed first
        while (len(nodeStack) > 0):

            node = nodeStack.pop()
            currSum = node.treeSum

            if(currSum == targetSum and node.left is None and node.right is None):
                return True

            # Push right and left children of the popped node
            # to stack
            if node.right is not None:
                node.right.treeSum = currSum + node.right.val
                nodeStack.append(node.right)
            if node.left is not None:
                node.left.treeSum = currSum + node.left.val
                nodeStack.append(node.left)

        return False