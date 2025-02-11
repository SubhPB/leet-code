/**
 * 2948. Make Lexicographically Smallest Array by Swapping Elements
You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.
An array a is lexicographically smaller than an array b if in the first position where a and b differ,
 array a has an element that is less than the corresponding element in b.
  For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.
Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
 
npx ts-node ./src/app/2025/Feb/2948.ts
 */

class Solve2948{
    constructor(public nums:number[],public limit:number){
        this.nums = nums; this.limit = limit;
    };
    solution1(){
        const nums = this.nums, lm = this.limit;
        const groups :number[][] = [], groupMap: {[k:string]:number} = {};
        const abs = (val:number) => val<0?-val:val, lastIndex = (arr:any[]) => arr.length-1;
        for(let sn of [...nums].sort((a,b)=>a-b)){
            const glen = groups.length;
            if (!glen||abs(sn-groups[glen-1][lastIndex(groups[glen-1])])){
                groups.push([])
            };
            groups[lastIndex(groups)].push(sn);
            groupMap[sn]=groups.length-1;
        }
        const res:number[] = [];
        for(let n of nums){
            let j = groupMap[n];
            res.push(groups[j].shift()!)
        };
        return res
    };
    solution2(){
        const n = this.nums.length;
        const sortedNums = this.nums.map((num,i)=>[num,i]).sort(([n1],[n2])=>n1-n2), abs = (a:number,b:number) => {
            const diff = a-b;
            return diff>0?diff:-diff
        };
        let left = 0;
        while(left<n){
            let right = left+1;
            while(
                right<n&&abs(
                    sortedNums[right][0], sortedNums[right-1][0]
                ) <= this.limit
            ){
                right++;
            };
            const group = sortedNums.slice(left,right);
            const groupElemIndexes = group.map(([num,pos])=>pos).sort((a,b)=>a-b);
            for(let i=0; i<group.length; i++) this.nums[groupElemIndexes[i]] = group[i][0];
            left=right
        };
        return this.nums
    }
};

(
    ()=>{
        const ARGS:[number[],number][] = [
            [[1,5,3,9,8], 2],
            [[1,7,6,18,2,1], 3],
        ];
        ARGS.forEach(([nums,lm])=>console.log(
            `Leetcode-2948 nums=[${nums.join(', ')}] limit=${lm} solution -> [${new Solve2948(nums,lm).solution2().join(', ')}]`
        ))
    }
)()