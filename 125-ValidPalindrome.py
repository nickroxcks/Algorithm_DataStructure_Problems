'''
Two pointer one single loop, no extra memory

The idea here is to have two pointers, one at the begining and one at the end,  scan the string
until the two pointers meet in the middle to determine if we have a palindrome or not

O(N/2) = O(n) time
O(1) memory

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            left = s[p1]
            right = s[p2]

            if not left.isalnum():
                p1 +=1
            elif not right.isalnum():
                p2 -=1
            elif left.lower() != right.lower():
                return False
            else:
                p1 +=1
                p2 -=1
        return True