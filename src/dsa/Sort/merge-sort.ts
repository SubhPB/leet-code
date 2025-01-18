/**
 * Merge sort 
 * npx ts-node ./src/dsa/Sort/merge-sort.ts
 */


class MergeSort{
    constructor(public nums:number[]){
        this.nums = nums
    };
    sort1(){
        
        const fn = (arr=this.nums):number[] => {
            const n = arr.length, mid = Math.floor(n/2);
            if (n===1) return arr;

            const sorted1 = fn(arr.slice(0, mid));
            const sorted2 = fn(arr.slice(mid, n));

            const sortedArr :number[] = []

            let i=0, j=0;

            while(i<mid&&j<(n-mid)){
                if (sorted1[i]<sorted2[j]){
                    sortedArr.push(sorted1[i]);
                    i++
                } else {
                    sortedArr.push(sorted2[j]);
                    j++
                }
            };

            //computing left-overs
            if (i<mid) sortedArr.push(...sorted1.slice(i,mid));
            if (j<(n-mid)) sortedArr.push(...sortedArr.slice(j, n-mid)) 

            return sortedArr
        };
        return fn()
    };
};


(
    ()=>{
        const ARGS = [
            [35, 50, 15, 25, 80, 0, 90, 45],
            [35, 4,3, 4, 3, 2, 1]
        ];
        ARGS.forEach((nums)=> console.log(`Merge-sort nums=${nums} -> Solution: ${new MergeSort(nums).sort1()}`))
    }
)()