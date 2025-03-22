/**
 * 2401. Longest Nice Subarray

You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 
npx ts-node ./src/app/2025/Mar/2401.ts
 */

class Solve2401{
    constructor(public nums:number[]){
        this.nums=nums
    };
    solution(nums=this.nums){
        const n = nums.length;
        if (n<=1) return n;
        const dp = Array.from({length:n}, (_,i)=>Array.from({length:n}, (_,j)=> i===j ? true : false));
        let res = 1;
        for(let i=n-2; i>=0; i--){
            for(let j=i+1; j<n; j++){
                if (
                    (nums[i]&nums[j])===0
                    && dp[i+1][j] && dp[i][j-1]
                ){
                    //dp[i] points to subArr who starts nums[i] and whose last elem is nums[j]
                    /**Consider a subArray [3,8,48,10]
                     * To determine if this satisfy our problem statement. 
                     * [1]. 3 & 10 should equal 0
                     * [2]. [3,8,48] should be a true subArr who satisfy problem statement
                     * [3]. [8,48,10] should be also be true who satisfy problem statement 
                     * if all those conditions are true then we can conclude this subArr as true, means dp[i][j] = true
                     */
                    dp[i][j] = true
                    res = Math.max(res, j-i+1)
                }
            }
        };
        return res
    };
    solution2(nums=this.nums){
        /**
         * Key insights: 
         * 1. If no bits occurs at same position then AND will result into zero.
         * 2. (Revision) OR to set the bit, XOR to unset that value
         * Why don't we implement this in sliding window as strate
         */
        const n=nums.length;
        let curr=0, l=0;
        let res=0;
        for(let r=0; r<n; r++){
            while(curr & nums[r]){
                curr ^= nums[l];
                l++;
            };
            res = Math.max(res, r-l+1);
            curr |= nums[r]
        };
        return res      
    }
};

(
    ()=>{
        const ARGS = [
            [1,3,8,48,10],
            [3,1,5,11,13],
            [1,1]
        ];
        ARGS.forEach(nums => console.log(`Nums=${nums.join(', ')} Solution=${new Solve2401(nums).solution2()}`))
    }
)()