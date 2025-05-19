/**
 * 
3337. Total Characters in String After Transformations II

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"
Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

Output: 8

Explanation:

First Transformation (t = 1):

'a' becomes 'bc' as nums[0] == 2
'z' becomes 'ab' as nums[25] == 2
'b' becomes 'cd' as nums[1] == 2
'k' becomes 'lm' as nums[10] == 2
String after the first transformation: "bcabcdlm"
Final Length of the string: The string is "bcabcdlm", which has 8 characters.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 109
nums.length == 26
1 <= nums[i] <= 25

 npx ts-node ./src/app/2025/May/3337.ts
 */

class Solve3337{
    constructor(public s:string,public t:number, public nums:number[]){
        this.s=s; this.t=t; this.nums=nums;
    };
    solution1(s=this.s, t=this.t, nums=this.nums){ //Runs well, but better if we can reduce complexity to avoid runtime error for huge input
        const MOD = 10**9+7;
        let res = 0;

        const dp:number[][] = Array.from(
            {length:26}, (_, code)=> Array.from(
                {length:t+1}, (_,lvl) => {
                    if (lvl<=1){
                        return lvl===0 ? 0 : nums[code]
                    };
                    return -1
                }
            )
        );

        /**Sort, so that we first solve smaller problem and use those results later to solve bigger problems */
        const strArr = s.split('').sort((a,b) => nums[a.charCodeAt(0)] - nums[b.charCodeAt(0)]);

        const countChildren = (lvl:number,charCode:number) => {
            if (dp[charCode][lvl]===-1){
                let children = 0;
                for(let childCode=0; childCode<nums[charCode]; childCode++){
                    children = (children + countChildren(lvl-1, (charCode + childCode + 1)%26))%MOD;
                };
                dp[charCode][lvl] = children;
            };
            return dp[charCode][lvl]
        }

        for(let char of strArr){
            res = (
                res + countChildren(t, char.charCodeAt(0)-97)
            )%MOD;
        };
        return res
    };
    solution2(s=this.s, t=this.t, nums=this.nums){
        const MOD = 1e9+7, n = s.length;

        const modADD = (a:number,b:number) => ((a%MOD) + (b%MOD))%MOD;
        const modMUL = (a:number,b:number) => ((a%MOD) * (b%MOD))%MOD;
        const codeAt = (char:string) => (char.charCodeAt(0)-97)%26;
        
        const freq:number[] = Array(26).fill(0);
        for(let char of s) freq[codeAt(char)]+=1;
        
        const MATRIX = (
            m:number,
            n:number,
            inp:number|((i:number,j:number)=>number)
        ) => {
            const M = Array.from(
                {length:m},
                (_,mi) => Array.from(
                    {length:n}, 
                    (_,ni) => typeof inp === 'number' ? inp : inp(mi,ni)
                )
            );
            return M
        };

        const matrixMUL = (M1:number[][], M2:number[][]) => {
            const [[a,b], [c,d]] = [M1,M2].map(M=>[M.length, M[0].length]);
            if (b!==c) throw new Error(`Hey stupid!, M1[${a},${b}] can't be multiplied with M2[${c},${d}], ${b} != ${c}`);
            return MATRIX(
                a,
                d,
                (mi,ni) => {
                    let res = 0;
                    for(let i=0; i<b; i++) res = modADD(
                        res, modMUL(M1[mi][i], M2[i][ni])
                    );
                    return res
                }
            );
        };

        const matrixExp = (M:number[][], pow:number) => {
            let res = MATRIX(M.length, M[0].length, (mi,ni)=> mi===ni ? 1 : 0);
            while(pow>0){
                if (pow&1) res = matrixMUL(res, M);
                M = matrixMUL(M, M);
                pow >>= 1;
            }
            return res;
        };

        let Tm = MATRIX(26, 26, 0); //transformation matrix
        for(let alp=0; alp<26; alp++){
            for(let to=1; to<=nums[alp]; to++) Tm[alp][(alp+to)%26] = 1;
        };

        Tm = matrixExp(Tm, t); // 't' number of transformations
        
        const output = matrixMUL([freq], Tm);
        
        let cnt=0;
        for(let i=0; i<output[0].length; i++) cnt = modADD(cnt, output[0][i]);
        return cnt
    }
};

(
    ()=>{
        const ARGS: [string, number, number[]][] = [
            ["abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]],
            // ["azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
            // ["u", 5, [1,1,2,2,3,1,2,2,1,2,3,1,2,2,2,2,3,3,3,2,3,2,3,2,2,3]],
            // ["uc", 16, [5,3,1,6,4,9,6,6,7,3,10,6,8,4,1,5,3,5,5,2,10,7,6,6,5,10]]
        ];
        ARGS.forEach(
            ([s,t,nums]) => {
                const sol = new Solve3337(s,t,nums);
                console.log(`s="${s}" t=${t} Res=${sol.solution2()}`)
            }
        );
    }
)()