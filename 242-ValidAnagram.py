'''
O(n) time
O(1) memory

Using hashtable to keep track of count of letters.
Constant memory cause will have a max of 26 values in the hastable
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        #if length is not the same, we are done
        if(len(t)!= len(s)):
            return False

        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] = dict[s[i]] + 1
            else:
                dict[s[i]] = 1

            if t[i] in dict:
                dict[t[i]] = dict[t[i]] - 1
            else:
                dict[t[i]] = -1

        for letter in dict:
            if dict[letter] != 0:
                return False
        return True

'''
Sort Solution
O(nlogn) time, O(1) memory
'''
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
'''
Hash solution
First attempt not clean
O(n) time
O(1) memory
'''
class SolutionX:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for letter in s:
            if letter in dict:
                dict[letter] = dict[letter] + 1
            else:
                dict[letter] = 1

        for letter in t:
            if letter in dict:
                dict[letter] = dict[letter] - 1
            else:
                return False

        for letter in dict:
            if dict[letter] != 0:
                return False
        return True
