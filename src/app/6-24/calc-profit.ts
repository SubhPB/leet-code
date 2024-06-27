// Byimaan

/**
 * 
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3

 * CMD npx ts-node ./src/app/6-24/maximal-area/calc-profit.ts
 */

const prices = [3,3,5,0,0,3,1,4]

const calcProfit = () => {
    let maxProfit = 0;
    for(let i = 0; i < prices.length; i++){
        for(let j = i; j < prices.length; j++){
            let profit = prices[j] - prices[i];
            if (profit > maxProfit){
                maxProfit = profit;
            }
        }
    };
    return maxProfit
};

console.log(calcProfit())