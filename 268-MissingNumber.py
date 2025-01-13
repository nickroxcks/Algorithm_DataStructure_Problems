from typing import List

'''
My Solution
O(n) time
O(1) memory
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = 3 :
        # 3 + 2 + 1 = 6 = expected_sum
        # 3 + 0 + 1 = 4 = actual_sum
        # 6 - 4 = 2 = solution
        expected_sum = 0
        actual_sum = 0
        expected_sum_val = 0
        for num in nums:
            expected_sum += expected_sum_val
            expected_sum_val += 1
            actual_sum += num
        expected_sum += expected_sum_val
        return expected_sum - actual_sum