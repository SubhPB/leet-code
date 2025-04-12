/**
 * 2560. House Robber IV

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 
Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2

npx ts-node ./src/app/2025/Apr/2560.ts
 */

class Solve2560{
    constructor(public nums:number[],public k:number){
        this.nums=nums; this.k=k;
    };
    bfSolution(nums=this.nums,k=this.k){

        let Mn = Infinity;
        const n = nums.length;
        const bf = (i:number, h:number, mx:number) => {
            if (h===0) Mn = Math.min(Mn, mx);
            else if ((i + 2*(h-1)) >= n) return;
            else {
                bf(i+1, h, mx); //not-selected
                bf(i+2, h-1, Math.max(mx, nums[i]))//Selected
            }
        };
        bf(0, k, 0)
        return Mn
    };

    effSolution(nums=this.nums,k=this.k){
        const n = nums.length;
        const mins = [...nums].sort((a,b) =>a-b);
        
        const canDo = (i:number) => {
            let c = 0, last:number = -2 /**Just any invalid value.*/;
            const min = mins[i];
            for(let j=0; j<n;j++){
                if (c===k) break;
                const num = nums[j]
                if (num<=min && last+1 !== j){
                    c += 1;
                    last = j
                }
            };
            return c>=k
        };

        let left = k-1, right = n;

        while(left<right){
            const mid = Math.floor((left+right)/2);
            if (canDo(mid)){
                right=mid
            } else {
                left=mid+1
            }
        }

        return left<n ? mins[left] : -1
    }
};

(
    ()=>{
        const ARGS: [number[],number][] = [
            [[2,3,5,9], 2],
            [[2,7,9,3,1], 2]   
        ];
        ARGS.forEach(
            ([nums, k]) => console.log(
                `Nums=[${nums.join(',')}] K=${k} and BfSolution=${new Solve2560(nums,k).bfSolution()} and Eff-Solution=${new Solve2560(nums, k).effSolution()}`
            )
        )
    }
)()