/**
 * 3356. Zero Array Transformation II

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.


npx ts-node ./src/app/2025/Feb/3358.ts
 */


class Solve3358{
    constructor(public nums:number[],public queries:number[][]){
        this.nums=nums; this.queries = queries
    };
    solution(){
        const nums=this.nums, queries = this.queries, n=nums.length;
        let mask = 0;
        for(let i=0; i<n; i++) if (nums[i]) mask |= 1<<i;
        for(let k=0; k<queries.length; k++){
            const [l,r,maxval]=queries[k];
            for(let j=l; j<=r&&mask; j++){
                if (mask&1<<j){//if that spot is not zero
                    nums[j] = Math.max(0, nums[j]-maxval);
                    if (!nums[j]) mask ^= 1<<j; //nums[j] is now zero then update the mask
                }
            };
            if (!mask) return k + 1
        }
        return mask ? -1 : 0
    };
    solution2(){
        //Since our solution1 could produce strange result, if n is too big and will produce wrong mask
        const nums = this.nums, n=nums.length, queries=this.queries;
        let count = 0;
        for(let i=0; i<n; i++) if (nums[i]) count++;
        for(let k=0; k<queries.length; k++){
            const [l,r,maxval] = queries[k];
            for(let j=l; j<=r&&count; j++){
                if (nums[j]){
                    nums[j] = Math.max(0, nums[j]-maxval);
                    if (!nums[j]) count--;
                }
            };
            if (!count) return k+1
        }
        return count ? -1 : 0;
    }
};

(
    ()=>{
        const ARGS: [number[], number[][]][]  = [
            [[2,0,2], [[0,2,1],[0,2,1],[1,1,3]]],
            [[4,3,2,1], [[1,3,2],[0,2,1]]]
        ];
        ARGS.forEach(([nums, queries])=>console.log(`Nums=[${nums.join(', ')}] queries=[${queries.map(q=>`[${q.join(',')}]`).join(', ')}] Solution = ${new Solve3358(nums,queries).solution()}`))
    }
)()