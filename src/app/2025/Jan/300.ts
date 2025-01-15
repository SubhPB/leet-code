/**
 * 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

CMD npx ts-node ./src/app/2025/Jan/300.ts
 */

class Solve300{
    public n:number;
    constructor(public nums:number[]){
        this.nums=nums; this.n = this.nums.length;
    };
    solution1(){
        const dp = Array.from(this.nums, ()=>1/**min longest increasing subsequence must be 1*/);
        for(let i=this.n-1; i>=0; i--){
            for(let j=i+1; j<dp.length; j++) if (this.nums[i]<this.nums[j]) dp[i] = Math.max(dp[i],1+ dp[j])
        };
        return Math.max(...dp)
    }
};

(
    () => {
        const ARGS = [
            [10,9,2,5,3,7,101,18],
            [0,1,0,3,2,3]
        ];
        ARGS.forEach(nums => console.log(`\r\n nums=${nums}, longest common subsequence -> ${new Solve300(nums).solution1()}`))
    }
)()
