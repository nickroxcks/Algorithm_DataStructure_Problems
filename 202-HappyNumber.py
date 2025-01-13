'''
Leetcode Optimized Solution

Using floyds cycle algorithm
O(logn) time
O(1) memory
'''
class Solution3:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

'''
My solution
O(logn) time
O(logn) memory
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        sumval = n
        hashtable = set()
        while(sumval != 1):
            tempval = 0
            index = 0
            while (sumval - 10**index >= 0):
                digit = sumval // 10 ** index % 10
                tempval = tempval + digit**2
                index = index + 1
            if (tempval == 1):
                return True
            elif(tempval in hashtable):
                return False
            else:
                hashtable.add(tempval)
            sumval = tempval
        return True

'''
Cleaner version of my solution
'''
class Solution2:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

'''

'''
test = Solution()

print(test.isHappy(2))

#digit = 1902 // 10**2 % 10
#print(digit)