'''
O(n*m) time
O(1) memory
n = problem size
m = length of haystack

This is a brute force approach as we are performing nested for loop approach, where for each character in the haystack,
we are checking to see if that characters will lead to a substring that matches needle

This apporach is performed rather then a single one pass loop on order to catch special edge cases such as the word
"mississippi", where needles such as "issip" can appear inside other needles

28-FindTheIndexofFirstOccurenceString.py
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if (haystack[i + j] != needle[j]):
                    break
                if j == len(needle) - 1:
                    return i
        return -1
