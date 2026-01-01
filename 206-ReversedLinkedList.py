# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
My Solution:

Reverse list in single pass via remembering the previous node

O(n) time
O(1) memory
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev