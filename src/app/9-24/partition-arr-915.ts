/**
 * Byimaan
 * 
915. Partition Array into Disjoint Intervals

    Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

    Every element in left is less than or equal to every element in right.
    left and right are non-empty.
    left has the smallest possible size.
    Return the length of left after such a partitioning.

    Example 1:

    Input: nums = [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]
    Example 2:

    Input: nums = [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]

    CMD  npx ts-node ./src/app/9-24/partition-arr-915.ts
 */


function paritionDisjoint(nums = [5,0,3,8,6]){
    let rightArrIndex = 0;
    /** solution logic here */

    return nums.slice(0, rightArrIndex)
};

console.log(paritionDisjoint())