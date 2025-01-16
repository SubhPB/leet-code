/**
 * 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

CMD npx ts-node ./src/app/2025/Jan/300.ts
 */

class Solve300{
    public n:number;
    constructor(public nums:number[]){
        this.nums=nums; this.n = this.nums.length;
    };
    solution1(){
        const dp = Array.from(this.nums, ()=>1/**min longest increasing subsequence must be 1*/);
        //It's subsequence problem, solving left-to-right could be way harder than starting from right-to-left
        for(let i=this.n-1; i>=0; i--){
            for(let j=i+1; j<dp.length; j++) if (this.nums[i]<this.nums[j]) dp[i] = Math.max(dp[i],1+ dp[j])
        };
        return Math.max(...dp) // O(n^2)
    };
    solution2(){
        //Binary search approach to reduce time complexity
        const dp:number[] = [];
        for(let num of this.nums){
            //Our task is to find a dp[index] who is more or equals to current num
            let left = 0;
            let right = dp.length;
            while(left<right){
                const mid = Math.floor(
                    (left+right) / 2
                );
                if (dp[mid] >= num){
                    right=mid
                } else {
                    left=mid+1 
                }
            };
            if (left<dp.length){
                dp[left] = num
            } else dp.push(num)
        }
        return dp.length
    };
    solution3(){
        //This solution ios also based on dp, focused to find actual LIS array
        const n = this.nums.length
        // lisLength[i] means there last element of the LIS equals nums[i] then what would be the longest length that can be formed.
        //base case equals 1 because it is minimum obvious value
        const LISLength = Array.from(this.nums, ()=> 1);
        // prev, when lisLength[i] indicates length of longest-increasing-subsequence who ends with nums[i], then prev[i] indicates the previous element of the num[i] in sequence
        const prev = Array.from(this.nums, ()=>-1);

        let maxLenIndex = 0;

        for(let i=1; i<n; i++){
            for(let j=0; j<i; j++){
                //Time to update LISLength and prev
                if(this.nums[i]>this.nums[j]){

                    if (LISLength[i]<=LISLength[j]+1){
                        LISLength[i] = LISLength[j]+1;
                        prev[i] = j
                    };

                    if(LISLength[i]>LISLength[maxLenIndex]) maxLenIndex = i;

                };
            }
        };
        
        /** Now let's compute the actual LIS */
        let maxLength = LISLength[maxLenIndex], i = maxLenIndex;
        const LIS:number[] = Array.from({length:maxLength},()=>-1);

        for(let j=maxLength-1; j>=0; j--){
            LIS[j] = this.nums[i]
            i = prev[i]
        };

        return LIS
        
    }
};

(
    () => {
        const ARGS = [
            [0, 4, 12, 2, 10, 6, 9, 13, 3, 11, 7, 16],
            [4, 10, 4, 3, 8, 9, 1],
            [10,9,2,5,3,7,101,18],
            [0,1,0,3,2,3]
        ];
        ARGS.forEach(nums => console.log(`\r\n nums=${nums}, longest common subsequence -> ${new Solve300(nums).solution3()}`));

        // ARGS.forEach(nums => console.log(`\r\n nums=${nums}, longest common subsequence Solution-3 -> ${new Solve300(nums).solution3()} & Solution-2 -> ${new Solve300(nums).solution2()}`))

    }
)()
