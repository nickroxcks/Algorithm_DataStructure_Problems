/*

Linear one pass
O(n) time
O(1) memory
To max profit, you always want to be coparing against the current minimum price
since you of course can only buy on a future day.

*/
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {

    let minPrice = Infinity;
    let maxSell = 0;
    for(let i = 0; i < prices.length;i++){
        if(prices[i] < minPrice){
            minPrice = prices[i];
        }
        else if(prices[i] === minPrice){
            continue;
        }
        else{
            let profit = prices[i] - minPrice;
            if(profit > maxSell){
                maxSell = profit
            }
        }
    }
    return maxSell;
};