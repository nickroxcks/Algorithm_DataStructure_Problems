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



test = Solution()

print(test.lengthOfLongestSubstring('abcdefghijklmnopqrstuvwxyz'))