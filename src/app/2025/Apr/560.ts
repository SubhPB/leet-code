/**
 * 560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

npx ts-node ./src/app/2025/Apr/560.ts
 */

class Solve560{
    constructor(public nums:number[], public k:number){
        this.nums=nums; this.k=k;
    };
    solution(nums=this.nums, k=this.k){
        let sum = 0, res = 0;
        const prefix = new Map<number,number>();
        prefix.set(0,1);
        for(let num of nums){
            sum += num;
            const diff = sum-k;
            /**
             * k = sum - diff, there an array has sum of `k` if we can reduce diff from the `sum`
            */
            res += prefix.get(diff) || 0;
            prefix.set(
                sum, 
                1+(prefix.get(sum)||0)
            );
        };
        
        return res
    }
};


(
    ()=>{
        const ARGS:[number[],number][] = [
            [[1,1,1], 2],
            [[1,2,3], 3]
        ];
        ARGS.forEach(
            ([nums, k])=> {
                const sol = new Solve560(nums,k);
                console.log(`Nums=[${nums.join(',')}] K=${k} Ans=${sol.solution()}`)
            }
        )
    }
)()