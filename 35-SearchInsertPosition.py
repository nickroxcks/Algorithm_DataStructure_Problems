from typing import List


class Solution:

    '''
    Binary Search Solution

    O(logn) time
    O(1) memory
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
       left = 0
       right = len(nums) - 1

       if target < nums[left]:
            return left
       if target > nums[right]:
            return right + 1

       while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: #nums[mid] < target:
                left = mid + 1
       return left
    '''
    Array Solution
    O(n) time -> Worst case scan the entire array
    O(1) memory
    '''
    def searchInsertArray(self, nums: List[int], target: int) -> int:
        index = 0
        for num in nums:
            if num == target:
                return index
            else:
                if nums[index] > target:
                    return index
            index = index + 1
        return index
