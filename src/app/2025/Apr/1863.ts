/**
 * 1863. Sum of All Subset XOR Totals
Easy
Topics
Companies
Hint
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

 

Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
Example 3:

Input: nums = [3,4,5,6,7,8]
Output: 480
Explanation: The sum of all XOR totals for every subset is 480.
 

Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20

npx ts-node ./src/app/2025/Apr/1863.ts
 */

class Solve1863{
    constructor(public nums:number[]){
        this.nums=nums;
    };
    solution(nums=this.nums, n=nums.length){
        let res = 0;
        const map = new Map<number,number>();
        const queue = Array.from({length:n}, (_,i)=>1<<i);
        while(queue.length){
            const mask = queue.shift()!;
            let sf = Math.floor(Math.log2(mask)); //index of most significant bit!
            const xorSum = (
                mask & (mask-1)
            ) === 0 ? nums[sf] : map.get(mask)!;
            if (!map.has(mask)) map.set(mask, xorSum); 
            for(let i=sf+1; i<n; i++){
                const newMask = mask | 1<<i;
                const newXorSum = xorSum ^ nums[i];
                map.set(newMask, newXorSum);
                queue.push(newMask);
            };
            res += xorSum;
        }
        return res
    };
    solution2(nums=this.nums, n=nums.length){
        let weights = 0, occur = (2 ** n)/2;
        for(let num of nums){
            weights = weights | num
        }
        return occur * weights
    }
};


(
    ()=>{
        const ARGS = [
            [1,3],
            [5,1,6],
            [3,4,5,6,7,8]
        ];
        ARGS.forEach(nums => {
            const sol = new Solve1863(nums);
            console.log(`Nums=[${nums.join(', ')}] Ans=${sol.solution()} Eff-Solution=${sol.solution2()}`)
        })
    }
)()