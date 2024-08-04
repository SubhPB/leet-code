/**
 * BYIMAAN
 * 
 * 
 * # 140
Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

 CMD :- npx ts-node ./src/app/8-24/word-break-140.ts
 */

const S = "catsanddog", WordDict = ["cat","cats","and","sand","dog"];

function solveFindBreak(s:string = S, wordDict: string[] = WordDict){
    const output: string[] = [];

    const options = (char: string) => wordDict.filter(str => str.startsWith(char));
    const isValid = (i: number, option: string) => (
        (i + option.length <= s.length) && (
            s.slice(i, i+option.length) === option
        )
    );

    const recursion  = (i: number, value: string) => {
        
        if (i === s.length){
            output.push(value.trim());
            return
        };

        for(const option of options(s[i])){
            if (isValid(i, option)){
                recursion(
                    i+option.length,
                    value + " " + option
                )
            }
        }
    };

    recursion(0, '')

    return output
};

console.log(solveFindBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"]))