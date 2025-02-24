'''
My solution: Parallel iterative approach using 2 pointers and no additional memory
O(N+M) time
O(1) memory


'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Get the basic edge cases out of the way
        if (list1 is None and list2 is not None):
            return list2
        elif (list1 is not None and list2 is None):
            return list1
        elif (list1 == None and list2 == None):
            return list1

        head = ListNode()
        curr = head
        while (list1 is not None or list2 is not None):
            if (list1 and list2 and list1.val <= list2.val):
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif (list1 and list2 and list1.val > list2.val):
                curr.next = list2
                curr = curr.next
                list2 = list2.next

            elif (list1 and not list2):
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif (list2 and not list1):
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        return head.next
