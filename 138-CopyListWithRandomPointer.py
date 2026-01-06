
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

'''
My solution:

Two pass using hashtable

1) Create a empty dictionary, which will map oldNodes to their corresponding newNodes at the same position
2) Iterate through the old random list, where we create a brand new node each step of the way and store it as a value
in the hashtable with the oldNode as the key. The newNode will contain the old nodes same value
3) Iterate through the old random list once more, this time we are updating the corresponding newNodes random value to the node
we've already seen in the dictionary

Because we are mapping oldNode -> newNode, and the oldNode still contains its random pointer, we are able to update the newNodes random
to the same correct random position as the old list

Complexity Analysis:

O(2*n) = O(n) time
O(n) memory for storing the full lists in dictionary
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        # Stores oldNode -> NewNode
        nodes = {}
        oldNode = head
        prevNewNode = None

        while oldNode:
            newNode = Node(oldNode.val)
            if prevNewNode:
                prevNewNode.next = newNode
            nodes[oldNode] = newNode
            oldNode = oldNode.next
            prevNewNode = newNode

        oldNode = head
        newHead = nodes[head]
        newNode = nodes[head]
        while oldNode:
            if oldNode.random in nodes:
                newNode.random = nodes[oldNode.random]
            oldNode = oldNode.next
            newNode = newNode.next

        return newHead



