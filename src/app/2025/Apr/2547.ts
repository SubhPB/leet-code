/**
 * 2547. Minimum Cost to Split an Array

You are given an integer array nums and an integer k.

Split the array into some number of non-empty subarrays. The cost of a split is the sum of the importance value of each subarray in the split.

Let trimmed(subarray) be the version of the subarray where all numbers which appear only once are removed.

For example, trimmed([3,1,2,4,3,4]) = [3,4,3,4].
The importance value of a subarray is k + trimmed(subarray).length.

For example, if a subarray is [1,2,3,3,3,4,4], then trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4].The importance value of this subarray will be k + 5.
Return the minimum possible cost of a split of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,1,2,1,3,3], k = 2
Output: 8
Explanation: We split nums to have two subarrays: [1,2], [1,2,1,3,3].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1,3,3] is 2 + (2 + 2) = 6.
The cost of the split is 2 + 6 = 8. It can be shown that this is the minimum possible cost among all the possible splits.
Example 2:

Input: nums = [1,2,1,2,1], k = 2
Output: 6
Explanation: We split nums to have two subarrays: [1,2], [1,2,1].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1] is 2 + (2) = 4.
The cost of the split is 2 + 4 = 6. It can be shown that this is the minimum possible cost among all the possible splits.
Example 3:

Input: nums = [1,2,1,2,1], k = 5
Output: 10
Explanation: We split nums to have one subarray: [1,2,1,2,1].
The importance value of [1,2,1,2,1] is 5 + (3 + 2) = 10.
The cost of the split is 10. It can be shown that this is the minimum possible cost among all the possible splits.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
1 <= k <= 109

npx ts-node ./src/app/2025/Apr/2547.ts
 */

class Solve2547 {
    constructor(public nums:number[], public k:number){
        this.nums=nums; this.k=k;
    };
    /**
     * Solution1 is an example of outstanding attempt solution which tries to reduce official O(n^2) complexity near to O(n)
     * Works 90% but closely fails in some testcases, Even though this is not 100% correct, but (attempt-wise) far better than the original solution
     */
    solution1(nums=this.nums, k=this.k){
        const n = nums.length;
        const map = new Map<number,number>();

        /**When need make ith split 'shi[i]' gives the ideal index to do so*/
        const shi = [0, /**0 represent no spilt made, bar is in front of 0th index*/];
        for(let i=0; i<n; i++){
            const num = nums[i];
            if (!map.has(num)) map.set(num, 0);
            const currCount = map.get(num)!, newCount = currCount + 1;
            if (newCount>1){
                /**If need to make ith spilt, i-index is ideal */
                shi.push(i);
                map.clear();
            };
            map.set(num, 1);
        };

        map.clear();

        const pi = Array(n).fill(0); /**if a spilt at front of ith index pi[i] gives trimmed.length to the right */
        for(let i=n-1; i>=0; i--){
            const num = nums[i];
            map.set(num, map.has(num) ? map.get(num)!+1 : 1);

            if (i<n-1){
                const currCount = map.get(num)!;
                
                pi[i] = pi[i+1];
                if (currCount>1){
                    pi[i] += (currCount===2) ? 2 : 1
                };
            }
        };

        
        let min = Infinity;
        let barsUsed = 0;
        
        /**Min-value can't be found beyond the length of 'shi */
        for(let bar = 0; bar<shi.length; bar++){
            const subArrCount = bar + 1;
            barsUsed = min < (subArrCount * k) + pi[shi[bar]] ? barsUsed : bar
            min = Math.min(
                min,
                /**
                 * Consider if after 2 splits we got 3 subArrs.
                 * Then cost equals t1 + k + t2 + k + t3 + k
                 * const ithCut = shi[2]  //where shi[2] is ideal to make 2nd cur
                 * 3*k is obvious part of currMinValue, & t3 = pi[ithCut]]  
                 * All the values if ti are zero except t3
                */
               (subArrCount * k) + pi[shi[bar]]
            );
        }
        
        // console.log({pi, shi, barsUsed});
        
        // let splits:number[][] = []
        // for(let i=0; i<=barsUsed; i++){
        //     splits.push(nums.slice(shi[i], i===barsUsed ? n : shi[i+1]))
        // };
        // console.log('View: ', splits.map(split => `[${split.join(' ')}]`).join(' | '))
        return min
    };
    solution2(nums=this.nums, k=this.k){
        const n = nums.length;
        const memo = new Map<number, number>();

        const dp = (i:number) => {
            if (i===n) return 0;
            else if (memo.has(i)) return memo.get(i)!;

            let min = Infinity, cost = 0;
            const freq = new Map<number,number>();

            for(let bar=i; bar<n; bar++){
                const num = nums[bar];

                freq.set(
                    num, 
                    (freq.get(num) || 0) + 1
                );

                const count = freq.get(num)!;
                if (count>1){
                    cost += count===2 ? 2 : 1
                };

                const tempCost = cost + k + dp(bar+1);

                min = Math.min(
                    min, tempCost
                );
            };

            memo.set(i, min);
            return min
        };

        return dp(0)
    };
};

(
    ()=>{
        const ARGS: [number[], number][] = [
            // [[1,2,1,2,1,3,3], 2],
            // [ [1,2,1,2,1], 2],
            // [[1,2,1,2,1], 5],
            [[5,6,4,3,2,5,4,1,5,2,0,5,4,3,1,5,4,3,4,4], 3]
        ];
        ARGS.forEach(([nums,k]) => {
            const sol = new Solve2547(nums, k);
            console.log(`Nums=[${nums.join(', ')}] k=${k} MinCost=${sol.solution2()}`)
        })
    }
)()