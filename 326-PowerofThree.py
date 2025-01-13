'''
My solution

Runtime depends how fast log function is
n = 3**x
log3(n) = x
if log3(n) is whole number, return true
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n>0:
            e = math.log(n,3)
            x = round(e,1)
            if(pow(3,x)==n):
                return True 
            else:
                return False
        return False
