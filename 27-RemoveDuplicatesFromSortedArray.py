from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 0
        for rp in range(len(nums)):
            if lp == 0:
                lp += 1
                continue
            if nums[rp] > nums[lp - 1]:
                nums[lp] = nums[rp]
                lp += 1
        return lp
