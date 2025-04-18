/**
 * 962. Maximum Width Ramp
Medium
Topics
Companies
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 
npx ts-node ./src/app/2025/Mar/962.ts
 */


class Solve962{
    constructor(public nums :number[]){
        this.nums=nums;
    };
    solution(nums=this.nums){
        const n = nums.length;
        if (n<=1) return 0;
        const dp = Array.from({length:n+1}, (_,i)=>Array.from({length:n+1}, ()=>0));
        for(let i=1; i<n; i++){
            for(let j=i+1; j<=n; j++){
                const diff = nums[i]<=nums[j] ? j-i : 0;
                dp[i][j] = Math.max(diff, dp[i-1][j], dp[i][j-1])
            }
        }
        return dp[n-1][n]
    };
    solution2(nums=this.nums){
        const n = nums.length;
        let idealDiff = Math.max(0,n-1);

        const R:string[][] = []

        while(idealDiff>0){
            let start = 0, end = idealDiff;
            
            for(let i=idealDiff; i<n; i++){
                if (R.length<=start) R.push([])
                R[start].push(`(${start}-${i})`)
                if (nums[start]<=nums[end]){
                    for(let r of R){
                        console.log(JSON.stringify(r.join(', ')))
                    }
                    return idealDiff
                };
                start++; end++;
            };
            idealDiff--; //decrement because this value was not the max-diff
        };
        return idealDiff
    };
    solution3(nums=this.nums){
        /**Official one of the most-efficient algorithm */
        const n = nums.length;
        const maxRight = [...nums];
        for(let i=n-2; i>=0; i--) maxRight[i] = Math.max(maxRight[i], maxRight[i+1]);

        let res=0, left=0;
        for(let right=0; right<n; right++){
            while(nums[left]>maxRight[right]) left++;
            res = Math.max(res, right-left)
        }
        return res
    };
    solution4(nums=this.nums){
        //Not yet completed!
        const n = nums.length;
        const sdc:number[] = [];//strictly decreasing curve
        for(let i=0; i<n; i++){
            while(sdc.length&&nums[sdc[sdc.length-1]]<=nums[i]) sdc.pop();
            sdc.push(i)
        };
        console.log({sdc})
        let res = 0;
        for(let r=n-1; r>=0; r--){//traversing nums from right to left
            // console.log("Before %O",{r,sdc, res})
            while(sdc.length&&nums[sdc[sdc.length-1]]<nums[r]){
                res = Math.max(res, r - sdc.pop()!)
            };
            // console.log("After %O", {r,sdc,res})
        };
        return res;
    }
};


(
    ()=>{
        const ARGS = [
            [6,0,8,2,1,5],
            [9,8,1,0,1,9,4,0,4,1],
            [3, 4, 2, 5, 1, 6],
            [7,9,2,0,8,1]

        ];
        ARGS.forEach(nums => console.log(`Nums=[${nums.join(', ')}] Max-ramp=${new Solve962(nums).solution4()}`))
    }
)()