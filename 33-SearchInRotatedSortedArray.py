import math
from typing import List


'''
Leetcode iterative binary search one pass (optimal)
O(logn) time
O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


'''
My solution
Binary search one pass with recursion
O(logn) time
O(logn) memory for recursive call stack
'''
class Solution2:


    def search(self, nums: List[int], target: int) -> int:

        def BinarySearch(p1: int,p2: int,p3: int):

            if nums[p1] == target:
                return p1
            if nums[p2] == target:
                return p2
            if nums[p3] == target:
                return p3
            if p1 > p2 or p2 > p3:
                return -1
            print('couldnt find, continue searching. p1:',p1,'p2:',p2,'p3:',p3)
            '''
            We have not found it, so we determine if we search left or right branch
            '''
            if nums[p1] < nums[p2]:
                print('nums[p1] < nums[p2]')
                # must be in left subtree if this condition is met. Can't be in right
                if nums[p1] <= target and target <= nums[p2]:
                    return BinarySearch(p1+1,math.floor((p2-p1)/2) + p1,p2-1)

                # must be in right subtree. Can't be in left at this point
                elif p2 != p3:
                    print('here?')
                    return BinarySearch(p2 + 1, math.floor((p3-p2)/2) + p2, p3 - 1)

            # this must mean then nums[p2] <= nums[p3] since the array is sorted in asc
            elif nums[p2] < nums[p3]:
                print('nums[p2] < nums[p3]')
                if nums[p2] <= target and target <= nums[p3]:
                    return BinarySearch(p2+1,math.floor((p3-p2)/2) + p2, p3 - 1)
                elif p1 != p2:
                    return BinarySearch(p1 + 1, math.floor((p2-p1)/2) + p1, p2 - 1)

            # the pointers are equal and we still havent found the number. Means no solution.
            print('no solution found returning -1')
            return -1

        #p1 pointers at start, p2 at middle, p3 at end
        return BinarySearch(0, math.floor(len(nums)/2), len(nums)-1)



test = Solution()
nums = [4,5,6,7,0,1,2]
nums2 = [1]
nums3 = [3,5,1]
print(test.search(nums2,2))