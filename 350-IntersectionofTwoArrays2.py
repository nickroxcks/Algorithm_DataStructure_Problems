from typing import List

'''
My solution
O(n + m) time
O( min(n,m)  ) memory

hastable search
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        sol = []
        dic = {}

        for i in nums1:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        for i in nums2:
            if i in dic and dic[i] != 0:
                dic[i] = dic[i] - 1
                sol.append(i)
        return sol