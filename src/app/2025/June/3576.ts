/**
 * 3576. Transform Array to All Equal Elements

    You are given an integer array nums of size n containing only 1 and -1, and an integer k.

    You can perform the following operation at most k times:

    Choose an index i (0 <= i < n - 1), and multiply both nums[i] and nums[i + 1] by -1.

    Note that you can choose the same index i more than once in different operations.

    Return true if it is possible to make all elements of the array equal after at most k operations, and false otherwise.

    Example 1:

    Input: nums = [1,-1,1,-1,1], k = 3

    Output: true

    Explanation:

    We can make all elements in the array equal in 2 operations as follows:

    Choose index i = 1, and multiply both nums[1] and nums[2] by -1. Now nums = [1,1,-1,-1,1].
    Choose index i = 2, and multiply both nums[2] and nums[3] by -1. Now nums = [1,1,1,1,1].
    Example 2:

    Input: nums = [-1,-1,-1,1,1,1], k = 5

    Output: false

    Explanation:

    It is not possible to make all array elements equal in at most 5 operations.

    Constraints:

    1 <= n == nums.length <= 105
    nums[i] is either -1 or 1.
    1 <= k <= n

    npx ts-node ./src/app/2025/June/3576.ts
 */

class Solve3576{
    constructor(public nums:number[], public k:number){
        this.nums=nums; this.k=k
    };
    canMakeEqual(nums: number[], k: number): boolean {
        const n = nums.length;
        let pi=n, ni=n, pcnt=0;
        for(let i=0; i<n; i+=1){
            if (nums[i]>0){
                pi = Math.min(i, pi)
                pcnt+=1
            } else {
                ni = Math.min(i, ni)
            }
        };
        if ([0,n].includes(pcnt)) return true;

        const isEven = (x:number) => !(x&1);

        const countSwaps = (i:number, target:number) => {
            let s=0, curr=nums[i];
            while(i<n-1 && s<=k){
                if (curr===target){
                    curr = -nums[i+1];
                    s+=1
                } else {
                    curr = nums[i+1]
                };
                i+=1
            }
            return s<=k ? s : n+1;
        }

        let swaps = n+1;
        if (isEven(pcnt) && k>=(pcnt/2)){// -> pcnt/2 is at least swaps that will be needed!
            swaps = Math.min(swaps, countSwaps(pi, 1))// (target=1) when ever iterator see this value, that will swap it
        };
        if (swaps>k && isEven(n-pcnt) && k>=((n-pcnt)/2)){
            swaps = Math.min(swaps, countSwaps(ni, -1))
        };
        return swaps<=k
    };
}