# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


''''
My solution
Using hashtable to store memory addresses of each node
O(n) time
O(n) memory
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        currNode = head
        while (currNode):
            if id(currNode) in dic:
                return True
            else:
                dic[id(currNode)] = 1
                currNode = currNode.next
        return False

''''
Floyd's Cycle Finding Algorithm (Leetcode Solution)
The idea here is to have 2 pointers, 1 pointer which moves at double the pace of the other. Eventually,
if there is indeed a cycle, the two will intersect. If there is no cycle, then we reach a null node which 
will break the loop

O(n) time
O(1) memory
'''
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
