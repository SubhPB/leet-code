/**
 * 2354. Number of Excellent Pairs
You are given a 0-indexed positive integer array nums and a positive integer k.

A pair of numbers (num1, num2) is called excellent if the following conditions are satisfied:

Both the numbers num1 and num2 exist in the array nums.
The sum of the number of set bits in num1 OR num2 and num1 AND num2 is greater than or equal to k, where OR is the bitwise OR operation and AND is the bitwise AND operation.
Return the number of distinct excellent pairs.

Two pairs (a, b) and (c, d) are considered distinct if either a != c or b != d. For example, (1, 2) and (2, 1) are distinct.

Note that a pair (num1, num2) such that num1 == num2 can also be excellent if you have at least one occurrence of num1 in the array.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: 5
Explanation: The excellent pairs are the following:
- (3, 3). (3 AND 3) and (3 OR 3) are both equal to (11) in binary. The total number of set bits is 2 + 2 = 4, which is greater than or equal to k = 3.
- (2, 3) and (3, 2). (2 AND 3) is equal to (10) in binary, and (2 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
- (1, 3) and (3, 1). (1 AND 3) is equal to (01) in binary, and (1 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
So the number of excellent pairs is 5.
Example 2:

Input: nums = [5,1,1], k = 10
Output: 0
Explanation: There are no excellent pairs for this array.

 CMD npx ts-node ./src/app/2025/Jan/2354.ts
 */

class Solve2354{
    constructor(public nums:number[],public k:number){
        this.nums = nums; this.k = k;
    };
    intToBinary(num:number){
        return num.toString(2)
    };
    count(str:string,rep:string){
        return str.split(rep).length - 1
    };
    sum(arr:number[],fn=(acc=0,val=0)=>acc+val){
        return arr.reduce(fn,0)
    };
    AND(num1:number,num2:number){
        return parseInt(this.intToBinary(num1),2) & parseInt(this.intToBinary(num2),2)
    };
    OR(num1:number,num2:number){
        return parseInt(this.intToBinary(num1),2) | parseInt(this.intToBinary(num2),2)
    };
    solution1(){
        const numsSet = Array.from(new Set(this.nums));
        let excellentSets:number[][] = [];
        for(let num1 of numsSet){
            for(let num2 of numsSet){
                if(
                    (num1+num2) >= this.k
                    && (
                        this.sum([this.AND(num1,num2), this.OR(num1,num2)].map(this.intToBinary).map(binary=>this.count(binary,'1')))
                    ) >= this.k
                ) {
                    console.log({num1,num2,AND:this.AND(num1,num2),OR:this.OR(num1,num2), })
                    excellentSets.push([num1,num2])
                };
            }
        };
        return excellentSets.length
    }
};

(
    ()=>{
        const ARGS = [
            [[1,2,3,1], 3]
        ] as const;
        ARGS.forEach(
            //@ts-ignore
            ([nums,k]) => console.log(`\r\n nums=${nums} k =${k} and result -> ${new Solve2354(nums,k).solution1()}`)
        )
    }
)()