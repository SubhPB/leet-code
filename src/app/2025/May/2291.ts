/**
 * 2291 - Maximum Profit From Trading Stocks
    Posted on March 9, 2022 · 3 minute read
    Welcome to Subscribe On Youtube

    2291. Maximum Profit From Trading Stocks
    Description
    You are given two 0-indexed integer arrays of the same length present and future where present[i] is the current price of the ith stock and future[i] is the price of the ith stock a year in the future. You may buy each stock at most once. You are also given an integer budget representing the amount of money you currently have.

    Return the maximum amount of profit you can make.

    

    Example 1:

    Input: present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10
    Output: 6
    Explanation: One possible way to maximize your profit is to:
    Buy the 0th, 3rd, and 4th stocks for a total of 5 + 2 + 3 = 10.
    Next year, sell all three stocks for a total of 8 + 3 + 5 = 16.
    The profit you made is 16 - 10 = 6.
    It can be shown that the maximum profit you can make is 6.
    Example 2:

    Input: present = [2,2,5], future = [3,4,10], budget = 6
    Output: 5
    Explanation: The only possible way to maximize your profit is to:
    Buy the 2nd stock, and make a profit of 10 - 5 = 5.
    It can be shown that the maximum profit you can make is 5.
    Example 3:

    Input: present = [3,3,12], future = [0,3,15], budget = 10
    Output: 0
    Explanation: One possible way to maximize your profit is to:
    Buy the 1st stock, and make a profit of 3 - 3 = 0.
    It can be shown that the maximum profit you can make is 0.

    `npx ts-node ./src/app/2025/May/2291.ts`
 */

class Solve2291{
    constructor(public present:number[], public future:number[], public budget:number){
        this.present=present; this.future=future;
    };
    dpSol(present=this.present, future=this.future, budget=this.budget){
        const m = present.length;
        const DP = Array.from({length:budget+1}, ()=>0)

        for(let i=0; i<m; i++){
            const cost  = present[i];
            const gain  = future[i] - cost;      
            for(let currBud=budget; currBud>=cost; currBud-=1){
                DP[currBud] = Math.max(
                    DP[currBud], gain + DP[currBud-cost]
                )
            }
        }
        return DP[budget]
    }
};

(
    function(){
        const ARGS: [number[], number[], number, number][]= [
            [[5,4,6,2,3],  [8,5,4,3,5], 10, 6],
            [[2,2,5], [3,4,10], 6, 5],
            [[3,3,12], [0,3,15], 10, 0],
        ];
        ARGS.forEach(
            ([present, future, budget, expected]) => {
                const ans = new Solve2291(present, future, budget).dpSol();
                
                console.log(`Present=[${present.join(',')}], Future=[${future.join(',')}], Budget=${budget} Answer=${ans} [Test ${ans==expected ? "Passed" : "Failed"}!]`)
            }
        )
    }
)()