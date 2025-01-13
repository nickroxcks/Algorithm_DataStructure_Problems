import math
from typing import List

'''
My soltuion
O(n) time, O(1) memory
just use two pointers one from start and one from end
middle value does not need to move for odd numbered inputs

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        endIndex = len(s) - 1

        for i in range(math.floor(len(s)/2)):
            left = s[i]
            right = s[endIndex - i]
            s[i] = right
            s[endIndex-i] = left