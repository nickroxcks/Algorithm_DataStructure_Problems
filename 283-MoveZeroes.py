from typing import List


'''
Using two pointers, a slow and a fast pointer
fast pointer always moves up each iteration
O(n) time,
 O(1) memory
'''
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

'''
O(n) time
O(n) memory
using a reference array
'''
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ref_table = []

        for num in nums:
            if(num != 0):
                ref_table.append(num)

        for i, num in enumerate(nums):
            if i < len(ref_table):
                nums[i] = ref_table[i]
            else:
                nums[i] = 0



