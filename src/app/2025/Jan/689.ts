/**
 * 689. Maximum Sum of 3 Non-Overlapping Subarrays
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically smaller.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

 CMD npx ts-node ./src/app/2025/Jan/689.ts
 
 */

class Solve689 {
    public n :number;
    constructor(public nums:number[], public k:number){
        this.nums = nums, this.k = k; this.n = nums.length
    };
    recursiveSol(){
        if ([
            this.n === 0,
            this.k <= 0, 
            3*this.k<this.n
        ].every(v=>!!v)) return [];
        let resSubArray:number[] = [], resSubArraySum = 0;
        const arrSum = (a:number,b:number) => {
            if ([a,b].some(v => v>this.n || v<0)) throw new Error(`Invalid indices expected in range of [0,${this.n}] but got [${a},${b}]`);
            let sum = 0;
            for(let i=a; i<b; i++) sum += this.nums[i];
            return sum
        }

        const fn = (i:number, subArray:number[], subArraySum:number) => {
            if (subArray.length===3){
                if (subArraySum>resSubArraySum){
                    resSubArray = subArray;
                    resSubArraySum = subArraySum
                }
            } else if ( this.k*(3-subArray.length) <= this.n-i ){
                //selected
                fn(i+this.k, [...subArray, i], subArraySum+arrSum(i,i+this.k));
                //not-selected
                fn(i+1, subArray, subArraySum)
            }
        };
        fn(0, resSubArray, resSubArraySum);
        return resSubArray
    };
    topDownSolution(){
      const subArraysCount = 3;
      let subArrays :number[] = [], subArraysSum = 0;
      if (this.n>=subArraysCount*this.k && this.k>=1){
        const record : {[k:number]:number} = {};
        for(let i=0; i<=this.n-this.k; i++){
            record[i] = 0
            if (i===0){
                for(let j=0; j<this.k; j++) record[i] += this.nums[j];
            } else {
                record[i] = record[i-1] + this.nums[i+this.k-1] - this.nums[i-1]
            }
        };

        const fn = (i:number, arr:number[], arrSum:number) => {
            const remainingLength = this.k*(subArraysCount - arr.length);
            if (remainingLength===0){
                if (arrSum>subArraysSum){
                    subArraysSum = arrSum;
                    subArrays = arr;
                };
            } else if (remainingLength<=(this.n-i)){
                //select
                fn(i+this.k, [...arr, i], arrSum+record[i]);
                //not-selected
                fn(i+1, arr, arrSum)
            }
        };
        fn(0, subArrays, subArraysSum)
      };
      return subArrays  
    }
};

// const nums = [1,2,1,2,1,2,1,2,1], k = 2

const ARGS689: [number[], number][] = [
    [[1,2,1,2,6,7,5,1], 2],
    [[1,2,1,2,1,2,1,2,1], 2]
];
ARGS689.forEach(([nums,k]) => console.log(`\r\nLeetcode-689 nums=${nums}, k=${k} -> [${new Solve689(nums,k).topDownSolution()}]`))