# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # guaranteed each list has a size of minimium 1
        head = ListNode()
        cur_node = head
        p1 = l1
        p2 = l2
        carry = 0
        while (p1 or p2):

            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            sum_val = val1 + val2 + cur_node.val
            carry = 1 if sum_val >= 10 else 0
            sum_val = sum_val % 10

            cur_node.val = sum_val

            if (p1 and p1.next):
                p1 = p1.next
            else:
                p1 = None
            if (p2 and p2.next):
                p2 = p2.next
            else:
                p2 = None
            # p1 = p1.next if p1.next else None
            # p2 = p2.next if p2.next else None

            if (p1 or p2 or carry):
                new_node = ListNode(carry)
                cur_node.next = new_node
                cur_node = new_node

        return head