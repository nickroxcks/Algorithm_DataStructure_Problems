from typing import List

'''
My solution
One pass with hashmap
O(n) time, O(n/2) memory
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
                if dic[num] >= len(nums) / 2:
                    return num
            else:
                dic[num] = 1

'''
Boyer-Moore algorithm copied from leetcode
O(n) time, O(1) memory
'''
class Solution2:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate