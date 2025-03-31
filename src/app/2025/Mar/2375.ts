/**
 * 2375. Construct Smallest Number From DI String

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.


Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

npx ts-node ./src/app/2025/Mar/2375.ts
 */

class Solve2375{
    constructor(public pattern:string){
        this.pattern=pattern
    };
    solution(pattern=this.pattern,n=pattern.length){
        let lexMin = Infinity;
        const fn = (lex:string) => {
            if (lex.length===n+1) lexMin = Math.min(lexMin, parseInt(lex));
            else {
                const inc = pattern[lex.length-1] === 'I';
                const lastVal = parseInt(lex[lex.length-1])
                for(let i=1;i<=9;i++){
                    if (lex.includes(`${i}`)) continue;
                    if (inc&&i>lastVal) fn(lex+i);
                    if (!inc&&i<lastVal) fn(lex+i);
                }
            }
        };
        
        if (pattern.length) fn(pattern[0]==='I' ? '1' : `${n+1}`)
        return String(lexMin !== Infinity ? lexMin : '')
    };
    solution2(pattern=this.pattern, n=pattern.length){
        const res:number[] = [], stk:number[] = [];
        for(let i=0; i<=n; i++){
            stk.push(i+1);
            while(stk.length&&(
                (i===n || pattern[i]==='I')
            )) res.push(stk.pop()!)
        }
        return res.join('')
    }
};

(
    ()=>{
        const ARGS = [
            "IIIDIDDD",
            "DDD"
        ];
        ARGS.forEach(pattern => console.log(`pattern="${pattern}", lexMin="${new Solve2375(pattern).solution()}"`))
    }
)()