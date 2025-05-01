/**
 * 
2302. Count Subarrays With Score Less Than K

The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
Example 2:

Input: nums = [1,1,1], k = 5
Output: 5
Explanation:
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.

npx ts-node ./src/app/2025/Apr/2302.ts
 */

class Solve2302{
    constructor(public nums:number[], public k:number){
        this.nums=nums; this.k=k;
    };
    solution(nums=this.nums, k=this.k){
        const n = nums.length;
        const len = (a:number,b:number) => b>a ? b-a+1 : a-b+1;

        let i=0, j=0;
        let sum=0, res = 0;
        while(i<=j&&j<n){
            if (i===j) sum = nums[i];

            while(
                j+1<n
                &&(len(i,j+1)*(sum + nums[j+1]))<k
            ){
                sum += nums[j+1];
                j++;
            };

            if (i===j){
                if (sum<k) res+=1;
                i++;
                j++
            } else {
                res += len(i,j);
                sum -= nums[i]
                i++;
            };
        };
        return res
    };
};

(
    ()=>{
        const ARGS: [number[],number][] = [
            [[2,1,4,3,5], 10],
            [[1,1,1], 5]
        ];
        ARGS.forEach(
            ([nums, k]) => {
                const sol = new Solve2302(nums, k);
                console.log(`Nums=[${nums.join(',')}] K=${k} Sol=${sol.solution()}`)
            }
        )
    }
)()