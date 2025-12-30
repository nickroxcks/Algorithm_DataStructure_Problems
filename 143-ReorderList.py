'''
Naive Solution:

Utilize an array to store the linked list nodes in memory and remember the original order.
From there, utilize two pointers, one at the start and one at the end

O(n + n/2 ) = O(n) time
O(n) memory

'''
import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        mem = []
        while head:
            mem.append(head)
            head = head.next
        size = len(mem)
        index2 = size - 1

        for index, node in enumerate(mem):

            if index == math.floor(size / 2):
                node.next = None
                break
            node.next = mem[index2]
            index2 -= 1

            node.next.next = mem[index + 1]


