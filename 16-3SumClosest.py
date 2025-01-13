from typing import List

'''
two pointer with sort my solution
O(n^2) time, O(n) memory for the sorting
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        closest_diff = abs(target - closest_sum)
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                diff = abs(target - sum)
                if(abs(diff) < closest_diff):
                    closest_sum = sum
                    closest_diff = abs(diff)
                if sum > target:
                    hi -=1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif sum < target:
                    lo+=1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                else:
                    return target
        return closest_sum

test = Solution()
nums = [-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1]
print(test.threeSumClosest(nums,-14))
