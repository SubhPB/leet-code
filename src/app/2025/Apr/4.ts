/**
 * 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

npx ts-node ./src/app/2025/Apr/4.ts

 */


class Solve4{
    constructor(public nums1:number[], public nums2:number[]){
        this.nums1; this.nums2;
    };
    solution(n1=this.nums1, n2=this.nums2){
        const [nums1, nums2] = [n1,n2].sort((a,b) => a[0]-b[0]);
        let l = nums1.length - 1, r = 0;
        const midNums:number[] = [];

        let min = Infinity, max = -Infinity;
        while(l>=0 && r<nums2.length && nums1[l]>nums2[r]){
            const [tempMin, tempMax] = [nums1[l], nums2[r]].sort((a,b)=>a-b);
            min = Math.min(min, tempMin);
            max = Math.max(max, tempMax);
            midNums.push(tempMin, tempMax);
            l--;
            r++;
        };

        while(l>=0 && nums1[l]>min){
            midNums.push(nums1[l])
            l--;
        };
        while(r<nums2.length && nums2[r]<max){
            midNums.push(nums2[r])
            r++;
        };

        midNums.sort((a,b) => a-b)
        const l1 = l + 1;
        const l2 = l1 + midNums.length;
        const l3 = l2 + nums2.length - r;

        if (l3===0) return 0;

        const getNum = (i:number) => {
            if (i<l1) return nums1[i];
            else if (i>=l2) return nums2[r+i-l2];
            else return midNums[i-l1]
        }
        if (l3%2 === 0){
            const a = Math.floor((l3-1)/2), b = Math.ceil((l3-1)/2);
            return (getNum(a) + getNum(b))/2
        } else {
            const a = Math.floor(l3/2);
            return getNum(a)
        };
    };
};

(
    ()=>{
        const ARGS: [number[], number[]][] = [
            // [[0,0,0,0,0], [-1,0,0,0,0,0,1]],
            // [[2,2,4,4], [2,2,2,4,4]],
            [[1,3], [2,4,5,6]]
        ];
        ARGS.forEach(([nums1,nums2]) =>{
            const sol = new Solve4(nums1, nums2);
            console.log(`Nums1=[${nums1.join(',')}] Nums2=[${nums2.join(',')}] Sol=${sol.solution()}`)
        })
    }
)()