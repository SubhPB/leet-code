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



  function solveFindBreakDP(s: string, wordDict: string[]): string[] {
    const wordSet = new Set(wordDict);
    const dp: string[][] = Array(s.length + 1).fill(null).map(() => []);

    // Initialize the first position with an empty string to start building sentences
    dp[0] = [""];

    for (let end = 1; end <= s.length; end++) {
        for (let start = 0; start < end; start++) {
            const word = s.slice(start, end);
            if (wordSet.has(word)) {
                for (const sentence of dp[start]) {
                    dp[end].push(sentence + (sentence ? " " : "") + word);
                }
            }
        }
    }

    return dp[s.length];
}

/*
// Test cases
console.log(solveFindBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]));
console.log(solveFindBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]));
console.log(solveFindBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]));

dp[0]  = [""]
dp[1]  = []
dp[2]  = []
dp[3]  = ["cat"]
dp[4]  = ["cats"]
dp[5]  = []
dp[6]  = []
dp[7]  = ["cat sand", "cats and"]
dp[8]  = []
dp[9]  = []
dp[10] = ["cat sand dog", "cats and dog"]

 */