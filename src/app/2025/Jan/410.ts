/**
 * 410. Split Array Largest Sum
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

 npx ts-node ./src/app/2025/Jan/410.ts
 */

class Solve410{
    constructor(public nums:number[],public k:number){
        this.nums=nums; this.k=k;
    };
    canSplit(largest:number){
        /**
         * Task is whether we can split this.nums into `k` number of sub-arrays, so that each subArray's sum is equals/less than given `largest` 
         */
        let noOfSubArr = 0;
        let currSum = 0;
        for(let num of this.nums){
            currSum+=num;
            if(currSum>largest){
                noOfSubArr += 1;
                currSum = num
            }
        };
        // (noOfSubArr + 1) because if dividers equals 4 that would mean 5 subArrs
        return noOfSubArr + 1 <= this.k
    }
    solution1(){
        //This is basically a binary search problem;
        const numsSum:number[] = [this.nums[0]];
        for(let i=1; i<this.nums.length; i++) numsSum.push(numsSum[i-1]+this.nums[i])

        let minPossibleAns = Math.max(...this.nums); //e.g when k = nums.length;
        let maxPossibleAns = numsSum[numsSum.length-1]; //e.g when k = 1
        let answer = maxPossibleAns;
        
        while(minPossibleAns<=maxPossibleAns){
            const midPossibleAns = Math.floor( 
                (minPossibleAns+maxPossibleAns) / 2
            );

            if (this.canSplit(midPossibleAns)){ //means we found a new maxPossibleAns
                answer = midPossibleAns;
                maxPossibleAns = midPossibleAns - 1;
            } else { //means we found a new minPossibleAns, because midPossible is not a valid answer 
                minPossibleAns = midPossibleAns + 1;
            }
        };
        return answer
    }
};

(
    ()=>{
        const ARGS = [
            [[7,2,5,10,8], 2],
            [[1,2,3,4,5], 2]
        ] as const;
        ARGS.forEach(
            ([nums, k]) => {
                //@ts-ignore
                console.log(`\r\n nums=${nums}, k=${k} solution -> ${new Solve410(nums,k).solution1()}`)
            }
        )
    }
)()