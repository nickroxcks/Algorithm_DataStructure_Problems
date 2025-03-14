from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxMoney = 0
        leftPointer = prices[0]
        for rightPointer in prices:
            if rightPointer == leftPointer:
                continue
            elif rightPointer < leftPointer:
                leftPointer = rightPointer
            else:
                profit = rightPointer - leftPointer
                if profit  > maxMoney:
                    maxMoney = profit
        return maxMoney