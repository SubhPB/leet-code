/**
 * 
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.
 */

class Solve2094{
    constructor(public digits:number[]){
        this.digits=digits;
    };
    solution(digits=this.digits){
        const res:number[] = [];
        const [evenHash, oddHash]: {[k:string]:number}[] = [{},{}];

        const setHash = (num:number, count:number) => {
            if (num&1) oddHash[num]=count;
            else evenHash[num]=count
        };
        const getHash = (num:number|string) => {
            if (typeof num === 'string') num = parseInt(num);
            if(num&1) return num in oddHash ? oddHash[num] : 0;
            else return num in evenHash ? evenHash[num] : 0;
        };

        for(let dgt of digits) setHash(dgt, getHash(dgt)+1);

        const evens = Object.keys(evenHash), odds = Object.keys(oddHash);
        const all = [...evens, ...odds];

        for(let e3 of evens){
            for(let i2 of all){
                for(let i1 of all){
                    if (parseInt(i1) === 0) continue;

                    const hash: {[k:string]:number} = {};
                    const nums = [i1, i2, e3];
                    nums.forEach(key => {
                        if (!(key in hash)) hash[key]=0;
                        hash[key]+=1;
                    });

                    if (nums.every(num => getHash(num)>=hash[num])){
                        res.push(parseInt(nums.join('')))
                    }
                }
            }
        }
        return res
    }
}