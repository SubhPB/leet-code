/**
 * Byimaan
 * 239. Sliding Window Maximum
    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.

    

    Example 1:

    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7

    CMD :- npx ts-node ./src/app/9-24/s-w-m-239.ts
 */

const SWM = (nums = [1,3,-1,-3,5,3,6,7], k = 3) => {

    if (k <= 1){
        return nums.length ? nums : [];
    }

    /** Solution logic */
    const output:number[] = [];
    const max = (arr: number[]) => arr.reduce( (acc, val) => acc > val ? acc : val, arr[0])

    for(let i = 0; i <= nums.length - k; i++){
        if (!i){
            const subArr = nums.slice(i, i + k);
            output.push(max(subArr))
        } else {
            /** optimize */
            const lastMax = output[output.length - 1], newNum = nums[i+k-1];
            if (lastMax > newNum){
                output.push(lastMax)
            } else {
                output.push(newNum)
            }
        }
    };
    return output
};
    

console.log(SWM(undefined, 0))