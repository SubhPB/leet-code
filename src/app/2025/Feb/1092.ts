/**
 * 1092. Shortest Common Supersequence 

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

 npx ts-node ./src/app/2025/Feb/1092.ts
 */
class Solve1092{
    constructor(public s1:string,public s2:string){
        this.s1=s1; this.s2=s2;
    };
    solution1(s1=this.s1,s2=this.s2){
        const m = s1.length, n = s2.length;
        const dp:number[][] =  Array.from({length:m+1}, ()=>Array.from({length:n+1}, ()=>0));
        
        //just run lcs algo.
        for(let i=1; i<=m; i++){
            for(let j=1; j<=n; j++){
                if (s1[i-1]===s2[j-1]){
                    dp[i][j] = 1 + dp[i-1][j-1]
                } else {
                    dp[i][j] = Math.max(
                        dp[i][j-1], dp[i-1][j]
                    )
                }
            }
        };

        const scs = [];
        let i=m, j=n;
        while(i>0&&j>0){
            if(s1[i-1]===s2[j-1]){
                scs.unshift(s1[i-1])
                i--; j--;
            } else {
                if (dp[i][j-1]>dp[i-1][j]) j--;
                else i--;
            }
        };

        //ensure we don't skip any remaining character, if loop not terminate at both i=0 and j=0
        while(i>0) scs.unshift(s1[--i]);
        while(j>0) scs.unshift(s2[--j]);

        return scs.join('')
        
    }
};

(
    ()=>{
        const ARGS = [
            ['abac', 'cab'],
            ['abcdefghi', 'cdgi']
        ];

        ARGS.forEach(([s1,s2])=>{
            console.log(`S1='${s1}', S2='${s2}' ${new Solve1092(s1,s2).solution1()}`)
        })
    }
)()