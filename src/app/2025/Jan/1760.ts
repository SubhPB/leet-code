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

const solve1760 = (nums:number[], maxOperations:number) => {
   const n = nums.length;
   if (n<=1 || maxOperations<=0) return 0;
   const partitions: {[k:number]:[number, number][]} = {};
   const getPartitions = (k:number) => {
      if (!(k in partitions)){
         partitions[k] = Array.from(
            {length:Math.max(0, Math.floor(k/2))}, (_,i) => [i+1, k-i+1])
      };
      return partitions[k]
   };
   nums.sort((a, b) => b-a)
   let MAX = nums[0]

   const place = (arr:number[], val:number) => {
      if (arr.length===0 || arr[arr.length-1]>=val){
         arr.push(val)
      } else if (arr[0]<=val){
         arr.unshift(val)
      } else {
         for(let i=1; i<arr.length-1; i++){
            if (arr[i-1]>=val&&arr[i+1]<=val) {
               arr = [
                  ...arr.slice(0,i+1),
                  val,
                  ...arr.slice(i, arr.length)
               ]
            }
         }
      };
      return arr
   }
   const fn = (sortedArray:number[], ops:number) => {
      const tempMax = sortedArray[0];
      if (ops===0 || tempMax<=1){
         if (tempMax<MAX) MAX = tempMax
      } else {
         const p = getPartitions(tempMax);
         for(let [a, b] of p){
            const newSortedArray = place(place(sortedArray, a), b);
            fn([...newSortedArray], ops-1)
         }
      }
   };
   fn(nums, maxOperations)
   for(let k in partitions){
      console.log(`key=${k}, value=${partitions[k]}`)
   }
   return MAX
};

console.log(`\r\n@Leetcode-1760`);
const TestArgs1760 : [number[], number][] = [
   [ [2, 4, 8, 2] ,4],
   [ [35, 50, 15, 25, 80, 0, 90, 45], 2 ]
];
TestArgs1760.forEach(([nums, ops]) => console.log(` nums=${nums}, maxOperations=${ops} -> ${solve1760(nums, ops)} `))
