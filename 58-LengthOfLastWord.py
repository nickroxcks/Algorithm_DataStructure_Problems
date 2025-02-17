'''
One pass loop starting at the last index of string.
Worst case we have to scan the entire string to find the word

O(n) time
O(1) memory
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0
        for letter in reversed(s):
            if letter != ' ' and count >= 0:
                count += 1
                continue
            elif letter == ' ' and count > 0:
                return count

        return count