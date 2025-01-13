# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
My naive solution. One pass with storing list in memory
O(n) time
O(n) memory
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        sz = 0
        cur_node = head
        mem = []
        while cur_node:
            sz += 1
            mem.append(cur_node)
            cur_node = cur_node.next
        if sz <=1:
            return None
        elif sz-n == 0:
            head = head.next
        else:
            prev = mem[sz - n - 1]
            deleted_node = mem[sz-n]
            prev.next = deleted_node.next

        return head