from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backtrack(curr: List[int], n):
            if len(nums) == n:
                sol.append(nums)
                return
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack(curr,n)
                    curr.pop()
        curr = []
        backtrack(curr, len(nums))
        return sol

