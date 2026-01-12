
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

'''
Leetcodes Optimal memory solution (come back to this and try to code it myself)

Utilizing the input list to to "weave" in new nodes, rather then using a dictionary and costing additional memory
O(n) time
O(1) memory
'''
class Solution2:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = (
                ptr_new_list.next.next if ptr_new_list.next else None
            )
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new

