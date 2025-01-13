class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    #requires s to be on len=1 minimum
    def isPalindromeArray(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        sol = ''
        solLen = 0
        for i in range(len(s)):
            #odd length case
            l,r = i,i
            while(l>=0 and r< len(s) and s[l] == s[r]):
                if(r-l+1) > solLen:
                    sol = s[l:r+1]
                    solLen = r-l+1
                l -= 1
                r+=1
            #even length cases
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > solLen:
                    sol = s[l:r + 1]
                    solLen = r - l + 1
                l-=1
                r+=1

        return sol
    '''
    O(n^3) time
    It works, but very slow
    '''
    def longestPalindromeSlow(self, s: str) -> str:
        sol = ''
        for idx, letter in enumerate(s):
            curr_str = ''
            for j in range (idx, len(s)):
                curr_str = curr_str + s[j]
                if(self.isPalindromeArray(curr_str) == True):
                    if(len(curr_str) >= len(sol)):
                        sol = curr_str
        return sol
test = Solution()
print('sol: ', test.longestPalindrome('racecar'))