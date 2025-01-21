/**
 * 76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


CMD npx ts-node ./src/app/2025/Jan/72.ts
 */

class Solve72{
    public tCounter: ReturnType<typeof this.counter>; public sCounter: ReturnType<typeof this.counter>;
    constructor(public s:string, public t:string){
        this.s=s; this.t=t; this.tCounter = this.counter(this.t); this.sCounter = this.counter(this.s)
    };
    count(char:string,str:string){
        return str.split(char).length-1
    }
    counter(str:string){
        const set = Array.from(new Set(str)), record : {[k: string]:number} = {};
        set.forEach(char => {
            record[char] = this.count(char, str)
        })
        return record
    };
    solution1(){

        const contains = (subStr:string|ReturnType<typeof this.counter>) => {
            //Does the passed substring contains this.t
            if (typeof subStr === 'string') subStr = this.counter(subStr);
            return Object.keys(this.tCounter).every(
                tKey => tKey in subStr && subStr[tKey] >= this.tCounter[tKey]
            )
        };
        if (contains(this.sCounter)){
            let n = this.t.length;
            // let's n is the length of result substring which lies as t.length <= n <= s.length
            const Cache = this.counter(this.s.substring(0, n))
            while(n<=this.s.length){
                if (n>0){ // we will basically reuse the existing Cache
                    const newChar = this.s[n];
                    if (newChar in Cache) Cache[newChar]++;
                    else Cache[newChar] = 1;
                };
                const localCache = Object.create(Cache);
                //iterating as sliding window
                for(let i=0; i<=(this.s.length-n); i++){
                    if (i>0){//reusing local cache
                        let newChar = this.s[n+i], prevChar = this.s[i-1];
                        if (newChar in localCache) localCache[newChar]++;
                        else localCache[newChar] = 1;
                        localCache[prevChar]--;
                    };
                    if (contains(localCache)) return this.s.substring(i, i+n+1)
                };

                n++;
            }
        }
        return ''
    };
    solution2(){
        if (!this.t.length||this.s.length<this.t.length) return "";

        const window: {[k:string]:number} = {};
        let have = 0, need = Object.keys(this.tCounter).length;
        let resIndex = -1, resLen = Infinity;
        let left = 0;

        for(let right=0; right<this.s.length; right++){
            const newChar = this.s[right];
            window[newChar] = 1 + (newChar in window ? window[newChar] : 0);
            if (
                newChar in this.tCounter && this.tCounter[newChar] === window[newChar]
            ) have+=1;

            while(have===need){
                const len = right-left+1;
                if (len<resLen){
                    resIndex=left; resLen = len
                };
                const charToDel = this.s[left];
                window[charToDel]--;

                if (charToDel in this.tCounter && window[charToDel]<this.tCounter[charToDel]) have--;
                left++;
            }
        };

        if (resIndex===-1) return "";
        return this.s.substring(resIndex, resIndex+resLen)
    }

};

(
    ()=>{
        const ARGS = [
            ["ADOBECODEBANC", "ABC"],
            ["ABC", "AABC"],
            ["ABCD", "ABCD"],
            ["CCBBAA", "ABCA"]
        ] as [string, string][]
        ARGS.forEach(
            ([s,t]) =>  console.log(`\r\n s=${s} t=${t}, solution -> ${new Solve72(s,t).solution2()}`)
        );
    }
)()