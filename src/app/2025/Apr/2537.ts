/**
 * 2537. Count the Number of Good Subarrays

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109

npx ts-node ./src/app/2025/Apr/2537.ts
 */


class Solve2537{
    constructor(public nums:number[], public k:number){
        this.nums=nums; this.k=k;
    };
    solution1(nums=this.nums,k=this.k){
        const n = nums.length;
        let res = 0;

        const sort = Array.from({length:n}, (_,i)=> i).sort((a,b) => nums[a]-nums[b]);
        const dict: {[k:string]:number} = {};

        const Sn = (count:number) => count * (count-1) / 2

        let i=0, kmax = 0;
        while(i<n){
            const num = nums[sort[i]];
            dict[num] = 1;
            while(i+1<n && num===nums[sort[i+1]]){
                dict[num]++;
                i++;
            };
            kmax += Math.max(0, Sn(dict[num]))
            i++
        };

        const traversed : {[k:string]:any} = {}

        const fn = (s:number, e:number,kpos:number, d:typeof dict) => {
            //'s' and 'e' are inclusive!
            if (kpos < k || e-s+1 < 2 || `${s}-${e}` in traversed) return;
            console.log({subArr: nums.slice(s,e+1), kpos, d})
            res += 1;
            traversed[`${s}-${e}`]=true

            const snm = `${nums[s]}`;
            fn(
                s+1,
                e,
                kpos - Math.max(0, Sn(d[snm]) - Sn(d[snm]-1)),
                {...d, [snm]: d[snm]-1}
            );
            const enm = `${nums[e]}`;
            fn(
                s,
                e-1,
                kpos - Math.max(0, Sn(d[enm]) - Sn(d[enm]-1)),
                {...d, [enm]:d[enm]-1}
            )
        };

        fn(0,n-1, kmax, dict);

        return res
    };
    solution2(nums=this.nums,k=this.k){
        const n = nums.length;
        const freq = new Map<number,number>();
        const Sn = (count:number) => Math.max(0, count * (count-1) / 2) 

        let left = 0, right = 0, res = 0, tempK = 0;
        while(left<n&&right<n){

            while(right<n&&tempK<k){
                const val = nums[right];
                freq.set(val, freq.has(val) ? freq.get(val)!+1 : 1);
                const fCount = freq.get(val)!
                tempK += (
                    Sn(fCount) /**new contribution */
                    - Sn(fCount-1) /**prev contribution */
                );
                right++;
            };
            while(left<right&&tempK>=k){
                res += n-right+1;

                const val = nums[left];
                freq.set(val, freq.get(val)!-1); /**lessening count */
                const fCount = freq.get(val)!;
                tempK -= (
                    Sn(fCount+1) /**prev contribution */
                    - Sn(fCount) /**new contribution */
                )
                left++;
            };
        };
        return res
    }
};

(
    ()=>{
        const ARGS: [number[],number][] = [
            // [[1,1,1,1,1], 10],
            // [[3,1,4,3,2,2,4], 2],
            [[2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], 11]
        ];
        ARGS.forEach(([nums, k]) =>{
            const sol = new Solve2537(nums, k);
            console.log(`Nums=[${nums.join(', ')}] K=${k} Solution=${sol.solution2()}`)
        })
    }
)()