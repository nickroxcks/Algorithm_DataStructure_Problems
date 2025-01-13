# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

'''
My version
O(n) time
O(1) memory

My version I was too lazy to restore the linked list to its original shape
But hey, I did solve it on my own
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        1) find the end of first half
        '''
        #find the total length
        total_len = 0
        cur_node = head
        while(cur_node):
            total_len += 1
            cur_node = cur_node.next
        if(total_len <= 1):
            return True

        #set an end pointer to the start of the second half
        cur_node = head
        num_start_first = math.ceil(total_len / 2) + 1
        num_pos = 1
        while(num_pos < num_start_first):
            cur_node = cur_node.next
            num_pos +=1
        ptr_start_second = cur_node

        print('total_len: ', total_len)
        print('ptr_start_second:',ptr_start_second.val)
        '''
        2)Reverse the second half
        1 -> 2 -> 2 -> 1
        1 -> 2 -> 2     None <- 2 <- 1
        '''
        cur_node = ptr_start_second
        prev_node = None
        while(cur_node):
            print('whiel curr node')
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        print('prev_node', prev_node.val)
        '''
        3)Determine if palindrome
        prev_node is the head of second
        '''
        ptr1 = head
        ptr2 = prev_node
        while(ptr2):
            print('ok')
            if(ptr2.val==ptr1.val):
                print('here')
                ptr1 = ptr1.next
                ptr2=ptr2.next
                continue
            else:
                print('here2')
                return False
        '''
        4 should also restore shape of the original linked list.
        Too lazy but this solution will at least return the right answer
        '''
        return True


'''
Optimized Leetcode Version
This version will also retore the linked list to its original form
O(n) time
O(1) memory
'''
class Solution2:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
