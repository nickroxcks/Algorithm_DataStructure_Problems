import collections
from typing import List

'''
Optimal character counting solution
O(NK) time
O(NK) memory
'''
class Solution3:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

'''
O(N * KlogK) time
O(NK) memory
'''
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
'''
O(n^3) solution
O(1) memory
Solution is too slow
'''
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        # if length is not the same, we are done
        if (len(t) != len(s)):
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        for curword in strs:
            isNew = True
            for j, curBucket in enumerate(sol):
                if self.isAnagram(curBucket[0], curword):
                    sol[j].append(curword)
                    isNew = False
                    break

            if isNew:
                sol.append([curword])

        return sol
