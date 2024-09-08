/**
 * Byimaan
 * 
    974. Subarray Sums Divisible by K
    Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.

    Example 1:

    Input: nums = [4,5,0,-2,-3,1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

    CMD :- npx ts-node ./src/app/9-24/subarr-sum-974.ts
 */

function subArrSum(nums = [4,5,0,-2,-3,1], k = 5) {
    
    const arrSum = (arr: number[]) => arr.reduce( (acc, val) => acc + val, 0)
    const isDivisible = (arr:number[]) => (arrSum(arr) % k) === 0;

    const subArrs: number[][] = [];

    for(let i = 0; i < nums.length; i++){
        for(let j = i; j < nums.length; j++){
            const subArr = nums.slice(i, j+1);
            if (isDivisible(subArr)){
                subArrs.push(subArr)
            }
        }
    };

    return subArrs

};

console.log(subArrSum());
