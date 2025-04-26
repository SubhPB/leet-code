/**
 * 2338. Count the Number of Ideal Arrays

You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

Constraints:

2 <= n <= 104
1 <= maxValue <= 104

npx ts-node ./src/app/2025/Apr/2338.ts
 */

class Solve2338{
    constructor(public n:number, public maxValue:number){
        this.n=n; this.maxValue=maxValue
    };
    solution(n=this.n, maxValue=this.maxValue){

        const mod = 1e9 + 7;

        const dp: number[][] = Array.from(
            {length:maxValue+1}, (_,r) => (
                Array.from({length:n+1}, (_, c) => {
                    if (r===maxValue || c===n) return 1;
                    return 0
                })
            )
        );

        let res = 1
        for(let r=maxValue-1; r>0; r--){
            for(let c=n-1; c>0; c--){
                let upperBound = r;
                while(upperBound <= maxValue){
                    dp[r][c] = (dp[r][c] + dp[upperBound][c+1]) % mod;
                    upperBound += r
                };
            };
            res = (res + dp[r][1]) % mod
        };

        return res 
    }
};

(
    ()=>{
        const ARGS = [
            // [2,5],
            // [5,3],
            // [184, 389],
            // [5878, 2900],
            [2747, 5606]
        ];

        ARGS.forEach(
            ([n,maxValue]) => console.log(`N=${n} MaxValue=${maxValue} Solution=${new Solve2338(n,maxValue).solution()}`)
        )

    }
)()