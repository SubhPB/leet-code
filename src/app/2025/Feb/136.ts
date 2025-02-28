/**
 * 136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
npx ts-node ./src/app/2025/Feb/136.ts
 */

class Solve136{
    constructor(public nums:number[]){this.nums=nums};
    solution(nums=this.nums){
        /**
         * Using XOR (If two inputs are same return false else true), e.g. a^a=0, a^0=a
         */
        let res = 0
        for(let num of nums) res ^= num
        return res
    }
};
(
    ()=>{
        const ARGS = [
            [2,2,1],
            [4,1,2,1,2],
            [1]
        ];

        ARGS.forEach(nums =>console.log(`nums=[${nums.join(', ')}], Unique Int = ${new Solve136(nums).solution()}`))
        
    }
)()