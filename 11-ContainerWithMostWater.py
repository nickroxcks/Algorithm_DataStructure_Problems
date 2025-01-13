from typing import List


class Solution:
    '''
    O(n) time
    O(1) memory
    Sliding pointer solution
    '''
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
    '''
    Brute Force O(n^2) time, O(1) memory
    Not fast enough. Calculate every possible area, and grab the maximum
    '''
    def maxAreaSlow(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea