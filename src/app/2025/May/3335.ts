/**
 * 
3335. Total Characters in String After Transformations I

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105

 npx ts-node ./src/app/2025/May/3335.ts
 */

class Solve3335{
    constructor(public s:string, public t:number){
        this.s=s; this.t=t;
    };
    solution(s=this.s,t=this.t){
        const n = s.length, MOD = 1e9+7;
        let res = 0;
        if (t>0){
            let freq = Array(26).fill(0);
            const modAdd = (a:number, b:number) => (a%MOD + b%MOD)%MOD;
            for(let char of s) freq[char.charCodeAt(0)-97] += 1;

            for(let tf=0; tf<t; t++){
                const currFreq = Array(26).fill(0);
                for(let code=0; code<26; code++){
                    if (code<25) currFreq[code+1] = freq[code];
                    else {
                        currFreq[0] = freq[25];
                        currFreq[1] = modAdd(freq[25], currFreq[1])
                    }
                };
                freq=currFreq;
            };

            for(let code=0; code<26; code++) res = modAdd(res,freq[code]);
        };
        return res
    }
};
(
    ()=>{
        const ARGS:[string, number][] = [
            ["abcyy", 2],
            ["azbk", 1],
        ];
        ARGS.forEach(
            ([S,t]) => {
                const sol = new Solve3335(S,t);
                console.log(`\ns="${s}" t=${t} res=`, sol.solution())
            }
        )
    }
)()