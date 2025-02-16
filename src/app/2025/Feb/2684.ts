/**
 * 2364. Count Number of Bad Pairs

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair
 if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
    The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
    The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
    The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
    The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
    There are a total of 5 bad pairs, so we return 5.

npx ts-node ./src/app/2025/Feb/2684.ts
 */

class Solve2684{
    constructor(public nums:number[]){ this.nums=nums; };
    /** 
     * This problem is super-easy to solve in O(n(n+1)/2) can be solved with very basic strategy and weak problem solver.
     * The most beautiful/challenging aspect for advance problem solver is to reduce it to O(n)
     * The following solution appreciates the used mathematical+outstanding coding approach to solve the problem,
     *  & inspires to think beyond just basics, tells good is enemy of better, better is enemy of best
     */
    solution1(){
        /**
         * Important aspect of the problem `j - i != nums[j] - nums[i].`
         *  could reminds us mathematical concept of `slope` ((y2-y1)/(x2-x1))
         *  It's basically saying y2-y1 should equals x2-x1 means fraction should be either 0 or 1.
         * Consider a graph with nums as y coordinate and index as x coordinate
         * Put the each pair into graph and see how many pairs are there lying under same slope, 
         * So we need to find # of good pairs under same slope for each slope value, which eventually would lead to #-of-bad-pairs.
         */
        let totalPairs = 0/**if n=4 e.g 3+2+1 */, goodPairs = 0;
        const count: {[k:string]:number} = {};
        for(let i=0; i<this.nums.length; i++){
            totalPairs += i;
            const slope = this.nums[i] - i;
            if (!(slope in count)) count[slope] = 0;
            goodPairs += count[slope];
            count[slope]++;
        };
        return totalPairs - goodPairs
    }
};

(
    ()=>{
        const ARGS = [
            [4,1,3,3]
        ];
        ARGS.forEach((nums)=>console.log(`Leetcode-2684 nums=[${nums.join(', ')}] badPairs=${new Solve2684(nums).solution1()}`))
    }
)()