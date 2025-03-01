/**
 * 
The Knuth-Morris-Pratt (KMP) algorithm solves the problem of finding occurrences of a "pattern" string within a larger "text" string. 
Given a text string T and a pattern string P, find all occurrences of P within T.
 The algorithm should be efficient, ideally with a time complexity significantly better than naive string matching.

 npx ts-node ./src/app/2025/Feb/kmp.ts
*/

class SolveKMP {
    constructor(public text:string[], public pattern:string[]){
        this.text=text; this.pattern=pattern
    };
    solution(text=this.text,pattern=this.pattern){
        const T = text.length, P = pattern.length;
        const lps = Array(P).fill(0);
        let i = 0, j = 1;
        while(j<P){
            if (pattern[i]===pattern[j]){ 
                lps[j] = i+1; //Or lps[j-1]+1;
                i++; j++; 
            }else{
                if (i!==0){
                    i = lps[i-1]
                } else{
                    lps[j] = 0;
                    j++
                }
            }
        };
        console.log(`LPS : %O`, lps)
        i=0; j=0;
        while(i<=T&&j<=P){
            if (j===P) return true;
            else if (i===T) break;
            else {
                if (text[i]===pattern[j]){
                    i++; j++;
                } else {
                    if (j===0){
                        i++;
                    } else {
                        j = lps[j-1]
                    }
                }
            }
        }
        return false
    }
};

(
    ()=>{
        const ARGS: [string,string][] = [
            ["abxabcabcaby", "abcaby"],
            ["abcdabcabcdf", "abcdf"]
        ];
        ARGS.forEach(([text,pattern])=>console.log(`Text=${text}, pattern=${pattern} lps : %O`, new SolveKMP(text.split(''),pattern.split('')).solution()))
    }
)()