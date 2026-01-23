'''
My Solution:

Sliding Window

We have a left and right pointer which set the boundary of the current window.
The window is the current valid substring with no repeating characters.

The right pointer moves up every iteration, and we use a set to remember if we saw the character already.

If at any point we find the window is not a "substring with no repeating characters", we keep moving
the left pointer and removing from our set up until the window condition is satisfied.

O(n) time
O(n) memory
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = 0
        left = 0
        chars = set()
        for right in range(0,len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            sol = max(sol, right - left + 1)
        return sol


