class Solution:
    def reverse(self, x):
        isPositive = 1 if x >=0 else -1
        index = 0
        sol = 0
        for c in map(int, str(abs(x))):
            sol = sol + c * (10**index)
            index +=1
            if isPositive == 1 and sol > 2**31 -1:
                return 0
            elif isPositive == -1 and sol > 2**31:
                return 0

        return sol*isPositive

test = Solution()
test.reverse(12345)