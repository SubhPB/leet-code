/**
 * 1012. Numbers With Repeated Digits

Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

Example 1:

Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: n = 1000
Output: 262
 CMD npx ts-node ./src/app/2025/Jan/1012.ts
 */

class Solve1012{
    constructor(public n:number){
        if (n>=1&&n<=10**9){
            this.n=n
        } else throw new Error(`Constraint Failed! expected n E [1,10^9] but found ${n}`)
    };
    countUniqueDigits(l:number):number{
        if (l<=0) return 1;
        let ans = 9;
        for(let i=0; i<(l-1); i++) ans*=(9-i)
        return ans + this.countUniqueDigits(l-1)
    }
    // solution1(){
    // }
};

(
    ()=>{
        const solve = new Solve1012(1)
        Array.from({length:5}).forEach(
            (_,i) => console.log(`\r\n When n=${i} then countUniqueDigits -> ${solve.countUniqueDigits(i)}`)
        )
    }
)()