from typing import List

'''
Linear scan with first number of range stored
O(n) time
O(1) memory
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        sol = []
        if not nums:
            return sol

        first = nums[0]
        isSequence = False

        for index, num in enumerate(nums, start = 0):
            if index+1 != len(nums) and nums[index+1] == num +1 and isSequence is False:
                isSequence = True
                first = num
            elif index+1 != len(nums) and nums[index+1] == num +1 and isSequence is True:
                isSequence = True
            elif index+1 != len(nums) and nums[index+1] != num +1 and isSequence is True:
                result = str(first) + "->" + str(num)
                sol.append(result)
                isSequence = False
            elif index+1 == len(nums):
                if isSequence:
                    result = str(first) + "->" + str(num)
                    sol.append(result)
                else:
                    sol.append(str(num))
            else:
                sol.append(str(num))
        return sol

