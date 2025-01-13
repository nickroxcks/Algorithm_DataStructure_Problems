from typing import List

'''
My solution
O(n) time
O(m) memory
use hashtable to detect 

 'A' ===>    hash('A') ==> 0X857899376   => 1

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = set()

        for num in nums:
            if(num in hashtable):
                return True
            else:
                hashtable.add(num)
        return False