/**
 * 3551. Minimum Swaps to Sort by Digit Sum

You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

Return the minimum number of swaps required to rearrange nums into this sorted order.

A swap is defined as exchanging the values at two distinct positions in the array.

Example 1:

Input: nums = [37,100]

Output: 1

Explanation:

Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 1.
Example 2:

Input: nums = [22,14,33,7]

Output: 0

Explanation:

Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
Thus, the minimum number of swaps required to rearrange nums is 0.
Example 3:

Input: nums = [18,43,34,16]

Output: 2

Explanation:

Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
nums consists of distinct positive integers.


 npx ts-node ./src/app/2025/May/3551.ts
 */

class Solve3551{
    constructor(public nums:number[]){
        this.nums=nums
    };
    solution(nums=this.nums){
        const n = nums.length;

        const dgtSumMem: {[k:string]:number} = {};
        const dgtSum = (dgt:number) => {
            if (!(dgt in dgtSumMem)){
                dgtSumMem[dgt] = `${dgt}`.split('').map(c=>parseInt(c)).reduce(
                    (acc,val) => acc+val, 0
                );
            };
            return dgtSumMem[dgt];
        }
        
        const fnl = Array.from({length:n}, (_,i)=>i);
        fnl.sort((a,b)=>nums[a]-nums[b]);
        fnl.sort((a,b)=>dgtSum(nums[a])-dgtSum(nums[b]));
        
        const curr = Array.from({length:n}, (_,i)=>i);
        const track = Array.from({length:n}, (_,i)=>i)

        let swaps = 0;
        for(let i=0; i<n; i++){
            if (curr[i]!==fnl[i]){
                swaps+=1;
                curr[track[fnl[i]]] = curr[i];
                track[curr[i]] = track[fnl[i]]
            }
        };
        return swaps
    };
    solution2(nums=this.nums){//Same as ist solution but uses cycle-detection to calculate swaps
        const n = nums.length;

        const dgtSumMem:{[k:string]:number} = {};
        const dgtSum = (dgt:number) => {
            if (!(dgt in dgtSumMem)){
                dgtSumMem[dgt] = `${dgt}`.split('').map(c=>parseInt(c)).reduce(
                    (acc,val) => acc+val, 0
                );
            };
            return dgtSumMem[dgt];
        };

        const to = Array.from({length:n}, (_,i)=>i);
        to.sort((a,b)=>nums[a]-nums[b]);
        to.sort((a,b)=>dgtSum(nums[a])-dgtSum(nums[b]));
        //to[i] = j, means At index i we need the original index 'j'

        const seen = Array(n).fill(false);
        let cycles=0;
        for(let i=0; i<n; i++){
            if (seen[i]) continue;
``
            let j=i;//We're at first unseen vertex of new cycle
            do{
                seen[j]=true;
                j=to[j]
            } while (!seen[j]);
            cycles+=1;
        };
        return n-cycles
    }
};

(
    ()=>{
        const ARGS = [
            // [18,43,34,16],
            [268835996,65052660,415128775],
            [277993448,416038674,616955867,539372283]
        ]
        ARGS.forEach(
            (nums) => {
                const sol = new Solve3551(nums);
                console.log(`Nums=[${nums.join(',')}] Swaps=${sol.solution()} Swaps2=${sol.solution2()}`)
            }
        )
    }
)()