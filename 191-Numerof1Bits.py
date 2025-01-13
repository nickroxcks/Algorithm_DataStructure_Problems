'''
My Solution
Bit Manipulation
o(1) time O(1) memory
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        numbits = 0
        mask = 1
        i=1
        while i<=32:
            if(n & mask):
                numbits = numbits + 1
            mask = mask <<1
            i = i + 1
        return numbits