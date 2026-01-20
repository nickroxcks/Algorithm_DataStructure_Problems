'''
My Solution: Sliding window

Utilize a left and right pointer, where the right pointer increases by 1 every iteration.

The left pointer keeps track of the lowest buy. If at any point we encounter an even lower buy,
update the left pointer to that postition

Time only moves forward, so it's safe to move the left pointer since we know anything that came earlier
no longer needs to be considered for buying

O(n) time
O(1) memory
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # The minimum value we are buying
        right = 1 # Current iteration
        max_profit = 0
        
        while (right < len(prices)):
            max_profit = prices[right] - prices[left] if prices[right] - prices[left] > max_profit else max_profit
            left = right if prices[right] < prices[left] else left
            right+=1

        return max_profit

