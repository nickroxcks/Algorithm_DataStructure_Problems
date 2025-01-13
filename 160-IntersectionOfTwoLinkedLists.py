'''
My Solution (two pointers)
O(n + m) time, O(1) memory
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        Acount = 0
        Bcount = 0
        while pa is not None:
            Acount = Acount + 1
            pa = pa.next
        while pb is not None:
            Bcount = Bcount + 1
            pb = pb.next

        i = 1
        pa = headA
        pb = headB
        while pa is not None or pb is not None:
            if (Acount >= Bcount):
                if (pa == pb):
                    return pb
                elif (i > (Acount - Bcount)):
                    if (pa is not None):
                        pa = pa.next
                    if (pb is not None):
                        pb = pb.next
                else:
                    if (pa is not None):
                        pa = pa.next
            else:
                if (pa == pb):
                    return pb
                elif (i > (Bcount - Acount)):
                    if (pb is not None):
                        pb = pb.next
                    if (pa is not None):
                        pa = pa.next
                else:
                    if (pb is not None):
                        pb = pb.next
            i = i + 1
        return None
'''
Leetcode Simplified flex code
O(n + m) time, O(1) memory
'''
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.

'''
My Hash table solution
O(n + m) time, O(n) memory
'''
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None