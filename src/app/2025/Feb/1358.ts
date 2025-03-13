/**
 * 1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1

npx ts-node ./src/app/2025/Feb/1358.ts
 */


class Solve1358 {
    constructor(public str:string){
        this.str=str;
    };
    solution(s=this.str){
        const n = s.length, map: {[k:string]:number} = {'a':0, 'b':0, 'c':0};
        const contains = () => ['a','b','c'].every(k=>map[k]>0);
        let count = 0;
        let i=0, j=0;
        while(j<n){
            map[s[j]]++;
            while(contains()){
                map[s[i++]]--;
                count += (n-j)
            };
            j++
        }
        return count
    };
};

(
    ()=>{
        const ARGS = [
            "abcabc",
            "aaacb",
            "abc"
        ];
        ARGS.forEach(s=>console.log(` s='${s}' solution = ${new Solve1358(s).solution()}`))
    }
)()