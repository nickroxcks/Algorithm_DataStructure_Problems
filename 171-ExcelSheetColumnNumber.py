from string import ascii_uppercase

'''
My solution
MAth solution
O(n) time, O(26) memory

'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # build dictionary to simplify code
        dic = {}
        value = 1
        for letter in ascii_uppercase:
            dic[letter] = value
            value = value + 1

        sum = 0
        index = len(columnTitle) - 1

        for letter in columnTitle:
            sum = sum + dic[letter] * (26**index)
            index = index - 1
        return sum


test = Solution()
print(test.titleToNumber('ZY'))
