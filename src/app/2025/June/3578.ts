/***
 * 3578. Count Partitions With Max-Min Difference at Most K

    You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

    Return the total number of ways to partition nums under this condition.

    Since the answer may be too large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [9,4,1,3,7], k = 4

    Output: 6

    Explanation:

    There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

    [[9], [4], [1], [3], [7]]
    [[9], [4], [1], [3, 7]]
    [[9], [4], [1, 3], [7]]
    [[9], [4, 1], [3], [7]]
    [[9], [4, 1], [3, 7]]
    [[9], [4, 1, 3], [7]]
    Example 2:

    Input: nums = [3,3,4], k = 0

    Output: 2

    Explanation:

    There are 2 valid partitions that satisfy the given conditions:

    [[3], [3], [4]]
    [[3, 3], [4]]
    

    Constraints:

    2 <= nums.length <= 5 * 104
    1 <= nums[i] <= 109
    0 <= k <= 109
    npx ts-node ./src/app/2025/June/3578.ts
 */

class Solve3578{
    constructor(public nums:number[], public k:number){
        this.nums=nums; this.k=k;
    }
    solution(nums=this.nums,k=this.k){
        const n = nums.length, M = 1e9+7;
        //dp[i] = # of valid ways to partition the prefix nums[0...i-1] where last segment exactly ends at position[i-1]
        //dp[n] = what are all valid ways to partition the entire nums array where last segment's end is nums[n-1]
        const dp = Array(n+1).fill(0);
        //dpPrefix[i] = dp[0] + dp[1] + ... + dp[i-1]. we can say dpPrefix[i] = Total # of valid partitions that occur before position[i]
        const dpPrefix = Array(n+2).fill(0);

        dp[0]=1;
        dpPrefix[1]=1;

        const modadd = (...x:number[]) => {
            let res=0;
            for(let val of x) res = (res%M + val%M)%M
            return res;
        };

        let left = 0;

        class Q{
            private h = 0;
            private t = -1;
            private q:number[] = [];
            length(){
                return this.t-this.h+1
            };
            at(i:number){
                if (i === -1) i = this.length()-1;
                if (i>=0 && i<this.length()){
                    return this.q[this.h+i]
                }
                else throw new Error(`Index out of bound expected to be less than ${this.length()} but found ${i}`);
            };
            popleft(){
                if (this.length()>0){
                    this.h += 1;
                }
                else throw new Error(`Can't perform popleft operation when queue is empty`);
            };
            push(val:number){
                this.q.push(val);
                this.t+=1;
            };
            pop(){
                if (this.length()>0){
                    this.t -= 1;
                    return this.q.pop()!;
                }
                else throw new Error(`Can't perform pop operation when queue is empty`);
            }
        }

        const mxqueue = new Q(), mnqueue = new Q(); // Monotonic max/min queues

        for(let right=0; right<n; right+=1){
            while (mxqueue.length() && mxqueue.at(0) < left) mxqueue.popleft();
            while (mnqueue.length() && mnqueue.at(0) < left) mnqueue.popleft();

            const num = nums[right];
            while (mxqueue.length() && nums[mxqueue.at(-1)] <= num) mxqueue.pop();
            while (mnqueue.length() && nums[mnqueue.at(-1)] >= num) mnqueue.pop();

            mxqueue.push(right);
            mnqueue.push(right);

            let diff = nums[mxqueue.at(0)] - nums[mnqueue.at(0)];
            while (diff > k){
                if (mxqueue.at(0) === left) mxqueue.popleft();
                if (mnqueue.at(0) === left) mnqueue.popleft();
                left += 1
                diff = nums[mxqueue.at(0)] - nums[mnqueue.at(0)];
            };

            //Hence now we've found a segment that ends at position[right] ands starts at position[left]
            dp[right+1] = dpPrefix[right+1] - dpPrefix[left];

            dpPrefix[right+2] = modadd(dpPrefix[right+1], dp[right+1]);
        };

        return dp[n]%M
    }
};

(
  ()=>{
    const ARGS:[number[], number][] = [
        [[9,4,1,3,7], 4]
    ];
    for(let [nums, k] of ARGS){
        const isLarge = nums.length>9
        console.log(`\nNums=[${nums.slice(0, Math.min(9, nums.length)).join(',')}${isLarge?' ...':''}] k=${k} answer=${new Solve3578(nums, k).solution()}`)
    }
  }  
)()