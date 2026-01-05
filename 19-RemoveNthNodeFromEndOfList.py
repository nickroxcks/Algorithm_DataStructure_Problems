# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
My Latest Solution:

Two pointer solution

1) Have a right pointer and left pointer, where the two pointers are (n-1) nodes apart
2) The right pointer moves to the next node each iteration, where the left node only moves after right has reached 
the nth node. For example if n=2 for a list of len() = 5, left will increase as soon as right reaches the third node
3) When the right pointer reaches the end, the left pointer is now at the node that needs to by removed from the end

O(n) time
O(1) memory

There is also a two pass solution which I will mention but not code out:

1) Find the len() of list by scanning the list once
2) Pass a second time, updating the len() - n node to skip to point to its new next node

O(2n) = O(n) time
O(1) memory
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        right = head
        left = head
        prev = head

        if head is None:
            return head
        while right.next:
            right = right.next
            count+=1
            if count > n:
                prev = left
                left = left.next

        if n == 1 and count == 1:
            head = None
        elif n == 1:
            prev.next = None
        elif n == count:
            head = head.next
        else:
            prev.next = left.next
        return head

'''
Naive solution. One pass with storing list in memory
O(n) time
O(n) memory
'''
class SolutionNaive:
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