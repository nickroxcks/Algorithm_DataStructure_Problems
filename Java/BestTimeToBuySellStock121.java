/*

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
 */

public class BestTimeToBuySellStock121 {
    public int maxProfit(int[] prices) {
        int sol = 0;
        int lp = 0;
        for(int rp = 0; rp < prices.length; rp++){
            if(prices[rp] == prices[lp]){
                continue;
            } else if (prices[rp] < prices[lp]) {
                lp = rp;
            }
            else{
                int profit = prices[rp] - prices[lp];
                if (profit > sol){
                    sol = profit;
                }
            }
        }
        return sol;
    }
}
