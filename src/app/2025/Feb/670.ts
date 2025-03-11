/**
 * 670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

npx ts-node ./src/app/2025/Feb/670.ts
 */

class Solve670 {
    constructor(public num:number){
        this.num = num;
    };
    solution(){
        const num = Array.from(this.num.toString()).map((s)=>parseInt(s)), n =num.length;
        for(let i=0; i<n-1; i++){
            let j = i+1;
            while(j<n&&num[i]>=num[j]) j++;
            if (j!==n){
                [num[i], num[j]] = [num[j], num[i]];
                break;
            }
        }
        return parseInt(num.join(''))
    }
};

(
    ()=>{
        const ARGS = [2763, 9973];
        ARGS.forEach(num => console.log(`Num = ${num}, Solution = ${new Solve670(num).solution()}`))
    }
)()