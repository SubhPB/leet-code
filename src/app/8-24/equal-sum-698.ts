/**
 * Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

CMD = npx ts-node ./src/app/8-24/equal-sum-698.ts
 */

function arrSum(arr: number[]) { return arr.reduce((acc, val) => acc+val, 0)};

class Solve {
    constructor(public nums: number[], public k: number){
        this.nums = nums;
        this.k = k
    };

    findSubsets(nums=this.nums, targetSum: number){
        const subsets: number[][] = [];

        function BT(i: number, subset: number[]){
            if (i === nums.length){
                return
            };
            if (arrSum(subset) === targetSum){
                subsets.push(subset);
                return
            };

            if (nums[i] <= targetSum - arrSum(subset)){
                // 2 choices
                BT(i+1, [...subset])
                BT(i+1, [...subset, nums[i]])
            } else {
                BT(i+1, [...subset])
            }
        };
        BT(0, [])
        return subsets
    }
};

const nums=[4,3,2,3,5,2,1], k=4;

console.log(new Solve(nums, k).findSubsets(nums ,5))