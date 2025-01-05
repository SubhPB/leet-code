/**
 * 
    1760. Minimum Limit of Balls in a Bag
    Medium

    You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

    You can perform the following operation at most maxOperations times:

    Take any bag of balls and divide it into two new bags with a positive number of balls.
    For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
    Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

    Return the minimum possible penalty after performing the operations.

    

    Example 1:

    Input: nums = [9], maxOperations = 2
    Output: 3
    Explanation: 
    - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
    - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
    The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
    Example 2:

    Input: nums = [2,4,8,2], maxOperations = 4
    Output: 2
    Explanation:
    - Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
    - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
    - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
    - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
    The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.
    
    CMD npx ts-node ./src/app/2025/Jan/1760.ts
 */

class Solve1760 {
   /**One thing that certain answer lies in between range [1, max(nums)] */
   constructor(public nums:number[], public maxOperations:number) {
      this.nums = nums; this.maxOperations = maxOperations;
   };
   countOperations(num:number, target:number, threshold:number=Infinity){
      let operations = 0;
      while(num>target){
         if(operations>threshold) return Infinity;
         num -= target;
         operations++
      }
      return operations
   };
   solution1(){
      let bestCase = 1, worstCase = Math.max(...this.nums);
      while(bestCase < worstCase){
         let operationsTakenToReachBestCase = 0;
         for(let num of this.nums){
            if (operationsTakenToReachBestCase>this.maxOperations) break;
            const ops = this.countOperations(num, bestCase, this.maxOperations-operationsTakenToReachBestCase);
            operationsTakenToReachBestCase += ops
         };
         if (operationsTakenToReachBestCase>this.maxOperations){
            bestCase++
         } else {
            break;
         }
      }
      return bestCase
   };
   binarySearchSolution(){
      /**Most optimal solution based on binary search */
      const canDivide = (maxBalls:number) => {
         //Just optimal solution of this.countOperations
         let ops = 0;
         for(let num of this.nums){
            ops += Math.ceil( (num-maxBalls) / maxBalls )
            if (ops>this.maxOperations) return false
         }
         return true
      };
      let low = 1, high = Math.max(...this.nums);
      let minCost = high;
      while (low < high){
         const median = Math.floor( (high+low) / 2 );
         if (canDivide(median)){
            //means `median` is an answer, but not sure if it is most optimal, if no then that optimal number should exist on the left side
            minCost = median;
            high = median;
         } else {
            //means optimal solution is bigger than `median`, then we need to check at right side (num who are greater than `median`)
            low = median + 1
         }
      }
      return minCost
   }
   solve = this.binarySearchSolution
}

console.log(`\r\n@Leetcode-1760`);
const TestArgs1760 : [number[], number][] = [
   [ [2, 4, 8, 2] ,4],
   [ [35, 50, 15, 25, 80, 0, 90, 45], 2 ]
];
TestArgs1760.forEach(([nums, ops]) => console.log(` nums=${nums}, maxOperations=${ops} -> (i) ${new Solve1760(nums, ops).binarySearchSolution()}, (ii) ${new Solve1760(nums, ops).solution1()} `))
