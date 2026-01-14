from typing import List

'''
Floyds cycle algorithm

If we think about it, we can form a natural linkedlist when we say each number in the list points to a
number in the list where the index corresponds to that numbers value.

Example: [1,3,4,2,2] 1 -> 3 -> 2 -> 4 -> ...

With this intuition,we see a cycle is formed in the linkedlist. Thus, we can utilize floyds algorithm
to find where the cycle starts and what is the duplicate number

Floyds algorithm is as follows:
1) Have a slow pointer and fast pointer. Slow pointer moves up 1 each iteration, fast pointer moves up 2. Stop when the
two pointers intersect
2) Keep the slow pointer, but now initialize a second slow pointer to point to the beigning of the list. Now
have both slow pointers move up by 1 each iteration until they intersect. The intersections yields the duplicate number.

O(n) time
O(1) memory
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        left = nums[0]
        while True:
            if left == slow:
                return left
            else:
                left = nums[left]
                slow = nums[slow]
