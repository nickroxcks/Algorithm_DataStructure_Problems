'''
My Solution (bad)
'''
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        dic = {}
        sol = []
        for i in range(n+1):
            count = 0
            j = i
            if j == 0:
                sol.append(0)
            while j:
                if j in dic:
                    sol.append(dic[j] + count)
                    exit
                if j % 2 == 1:
                    count += 1
                j = j//2
                if j == 0:
                    sol.append(count)
        return sol
