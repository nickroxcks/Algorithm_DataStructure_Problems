from typing import List

'''
My solution:

Create a Prefix array which computes products from the left
Create a Suffix array which computers products from the right
From there, we can multiply the corresponding element in the Prefix and Suffix array to 
find the product except self for every element in the solution

EX: 
nums = [1,2,3,4,5]
pre = [1,2,6,24,120]
suff = [5,20,60,120,120]

sol = [suff[-2], pre[0] * suff[-3], pre[1] * suff[-4], pre[2] * suff[-5], pre[3]]
sol = [120, 60, 40, 30, 24]

Complexity Analysis:

O(n) Time since we are computing 3 arrays each in a linear fashion
O(n) Memory as we need to store the 3 arrays in memory
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Computee Prefix Array
        pre = [nums[0]]
        for num in nums[1:]:
            pre.append(pre[-1] * num)

        # Computee Suffix Array
        suff = [nums[-1]]
        for num in reversed(nums[:-1]):
            suff.append(suff[-1] * num)

        # Compute Solution
        sol = []
        index = -1
        for suff_value in reversed(suff[:-1]):
            if index == -1:
                sol.append(suff_value)
            else:
                sol.append(pre[index] * suff_value)
            index +=1
        sol.append(pre[-2])
        return sol

'''
LeetCodes Optimal Solution

Same idea with a prefix and suffix array, but instad of using extra memory, 
we utilize the input and output arrays for storing the prefix and suffix array.

This allows us to achieve the same time complexity, but no additional memory since
the input and output arrays do not count as extra memory

Complexity Analysis
O(n) Time
O(1) Memory
'''
class SolutionOptimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer