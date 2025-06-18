/**
 * 3583. Count Special Triplets

    You are given an integer array nums.

    A special triplet is defined as a triplet of indices (i, j, k) such that:

    0 <= i < j < k < n, where n = nums.length
    nums[i] == nums[j] * 2
    nums[k] == nums[j] * 2
    Return the total number of special triplets in the array.

    Since the answer may be large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [6,3,6]

    Output: 1

    Explanation:

    The only special triplet is (i, j, k) = (0, 1, 2), where:

    nums[0] = 6, nums[1] = 3, nums[2] = 6
    nums[0] = nums[1] * 2 = 3 * 2 = 6
    nums[2] = nums[1] * 2 = 3 * 2 = 6
    Example 2:

    Input: nums = [0,1,0,0]

    Output: 1

    Explanation:

    The only special triplet is (i, j, k) = (0, 2, 3), where:

    nums[0] = 0, nums[2] = 0, nums[3] = 0
    nums[0] = nums[2] * 2 = 0 * 2 = 0
    nums[3] = nums[2] * 2 = 0 * 2 = 0
    Example 3:

    Input: nums = [8,4,2,8,4]

    Output: 2

    Explanation:

    There are exactly two special triplets:

    (i, j, k) = (0, 1, 3)
    nums[0] = 8, nums[1] = 4, nums[3] = 8
    nums[0] = nums[1] * 2 = 4 * 2 = 8
    nums[3] = nums[1] * 2 = 4 * 2 = 8
    (i, j, k) = (1, 2, 4)
    nums[1] = 4, nums[2] = 2, nums[4] = 4
    nums[1] = nums[2] * 2 = 2 * 2 = 4
    nums[4] = nums[2] * 2 = 2 * 2 = 4
    

    Constraints:

    3 <= n == nums.length <= 105
    0 <= nums[i] <= 105
    npx ts-node ./src/app/2025/June/3583.ts
 */

class Solve3583 {
    constructor(public nums:number[]){
        this.nums=nums;
    };
    specialTriplets(nums=this.nums){
        const n = nums.length, M = 1e9+7;
        const ADD = (x:number, y:number) => (x%M + y%M) % M;
        let res = 0;

        const indexes:{[k:string]:number[]} = {};
        const dp:{[k:string]:number} = {};

        const binarySearch = (desArr:number[], i:number) => {
            const m = desArr.length;
            /**Find index in desArr which such that desArr[index] < i and most closest to i*/
            if (m && desArr[m-1]<i){
                let l = 0, r = m-1; // desArr[r] always < i
                while (l<r){
                    const mid = Math.floor((l+r)/2);
                    if (desArr[mid]<i){
                        r=mid
                    } else {
                        l = mid+1
                    }
                };
                return l
            };
            return m
        };

        for(let x=n-1; x>=0; x-=1){
            const num = nums[x];
            if (!(num in indexes)) indexes[num] = [];

            const m = indexes[num].length, J = Math.floor(num/2);
            if (m && !(num&1)){//Only even num can contribute as special triplet
                const prevX = indexes[num][m-1]; //Most recent index where num has occurred
                
                const occJ = J in indexes ? indexes[J] : [];
                const prevJ = num>0 ? binarySearch(occJ, prevX) : 1;

                const cntJ = Math.max(0, occJ.length-prevJ)//How many times J has occurred before prevX
                const prevDp = num in dp ? dp[num] : 0;
                
                const cntX = num>0 ? m : 1;

                dp[num] = ADD(prevDp, cntJ*cntX)
                res = ADD(res, dp[num])

            }
            indexes[num].push(x);
        }
        return res;
    };
};

(
    ()=>{
        const ARGS:[number[], number][] = [
            [[6,3,6],1],
            [[0,1,0,0], 1],
            [[8,4,2,8,4], 2],
        ];
        ARGS.forEach(
            ([nums, exp]) => {
                const ans = new Solve3583(nums).specialTriplets();
                console.log(`Nums=[${nums.join(',')}] ans=${ans} expected=${exp} TEST-${ans===exp ? 'PASSED!':'FAILED!'}`)
            }
        )
    }
)()