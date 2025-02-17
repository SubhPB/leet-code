/**
 * 648. Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word
 - let's call this word derivative. For example, when the root "help" is followed by the word "ful",
  we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
 replace all the derivatives in the sentence with the root forming it.
  If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

npx ts-node ./src/app/2025/Feb/648.ts
 */

class Solve648{
    constructor(public dict:string[], public sentence:string){
        this.dict=dict.sort((a,b)=>a.length-b.length); this.sentence=sentence;
    };
    solution1(){
        const derivatives = this.sentence.split(" ");
        for(let i=0; i<derivatives.length; i++){
            const derivate = derivatives[i];
            const root = this.dict.find(rt=>derivate.startsWith(rt));
            if (root) derivatives[i] = root
        };
        return derivatives.join(" ")
    }
};

(
    ()=>{
        const ARGS: [string[], string][] = [
            [["cat","bat","rat"], "the cattle was rattled by the battery"],
            [["a","b","c"], "aadsfasf absbs bbab cadsfafs"]
        ];
        ARGS.forEach(([dict,sentence])=>console.log(`leetcode-684 dictionary=[${dict.join(", ")}] sentence=${sentence} solution=${new Solve648(dict,sentence).solution1()}`))
    }
)()