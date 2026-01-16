# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


'''
My Solution:

Linear scan while adding sums and storing carry values each step of the way

O(n) time
O(1) memory

'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = l1
        p2 = l2
        carry = 0
        solPrev = ListNode(0)
        prevNode = solPrev

        while p1 or p2 or carry:
            newNode = ListNode()

            val1 =  p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            curr_sum = val1 + val2 + carry

            if curr_sum >=10:
                curr_sum = curr_sum % 10
                carry = 1
            else:
                carry = 0

            newNode.val = curr_sum
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            prevNode.next = newNode
            prevNode = newNode

        return solPrev.next