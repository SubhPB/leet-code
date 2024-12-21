/**
 * Byimaan
 * 769. Max Chunks To Make Sorted
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible

CMD npx ts-node ./src/app/12-24/2182.ts
const unsortedArray = [23, 1, 45, 90, 2, 34, 67, 5, 88, 12, 0, -4, 17, 100, -10];
 */

const solve769 = (arr:number[]) => {
    let res = 0;
    let currMax = -1;
    arr.forEach(
        (val, ind) => {
            currMax = Math.max(val, currMax);
            if (currMax === ind) res++;
        }
    )
    return res
};

[
    [4,3,2,1,0],
    [1,0,2,3,4]
].forEach(
    arg => console.log(`\r\n Input = ${arg} Output = ${solve769(arg)}`)
)