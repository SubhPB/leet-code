/**
 * 962. Maximum Width Ramp
Medium
Topics
Companies
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 
npx ts-node ./src/app/2025/Mar/962.ts
 */


class Solve962{
    constructor(public nums :number[]){
        this.nums=nums;
    };
    solution(nums=this.nums){
        const n = nums.length;
        if (n<=1) return 0;
        const dp = Array.from({length:n+1}, (_,i)=>Array.from({length:n+1}, ()=>0));
        for(let i=1; i<n; i++){
            for(let j=i+1; j<=n; j++){
                const diff = nums[i]<=nums[j] ? j-i : 0;
                dp[i][j] = Math.max(diff, dp[i-1][j], dp[i][j-1])
            }
        }
        return dp[n-1][n]
    }
};


(
    ()=>{
        const ARGS = [
            [6,0,8,2,1,5],
            [9,8,1,0,1,9,4,0,4,1]
        ];
        ARGS.forEach(nums => console.log(`Nums=[${nums.join(', ')}] Max-ramp=${new Solve962(nums).solution()}`))
    }
)()