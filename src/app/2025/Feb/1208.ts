/**
 * 1208. Get Equal Substrings Within Budget
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

npx ts-node ./src/app/2025/Feb/1208.ts
 */

class Solve1208{
    constructor(public s:string, public t:string,public maxCost:number){
        this.s=s; this.t=t; this.maxCost = maxCost
    };
    utils={
        ascii(char:string){return char.charCodeAt(0)},
        abs(val:number){return val<0?-val:val}
    };
    solution1(){
        const s = this.s, t = this.t, l = s.length;
        const mod = (v:number) => v<0?-v:v;
        const costTable = Array.from(s).map((_,i)=>mod(s.charCodeAt(i)-t.charCodeAt(i)));
        let max = [0/*val*/, 0/*len*/, -1/*index*/], window = [...max]
        for(let i=0; i<l; i++){
            if ((l-i)<=max[1]) break; //if remaining length can't compete with pre-existing substring
            let size = 0,j = i;
            if (i>0){
                j = window[1]+i;
                size = window[0]-costTable[i-1]+costTable[j];
            }
            while(j<l&&(costTable[j]+size)<=this.maxCost){
                size+=costTable[j];
                if (size>=max[0]) max = [size, j-i+1, i];
                j++;
            };
            window = [size, j-i+1, i]
        };
        return max[1]
    };
    solution2(){
        const s = this.s, t = this.t;
        let currCost = 0, left = 0, res = 0;
        for(let right=0; right<s.length; right++){
            currCost += this.utils.abs(
                this.utils.ascii(s[right]) - this.utils.ascii(t[right])
            );
            while(currCost>this.maxCost){
                currCost -= this.utils.abs(
                    this.utils.ascii(s[left]) - this.utils.ascii(t[left])
                );
                left++;
            };
            res = Math.max(res, right-left+1)
        };
        return res;
    }
};

(
    ()=>{
        const ARGS:[string,string,number,number][] = [
            ["abcd", "bcdf", 3, 3],
            ["abcd", "cdef", 3, 1],
            ["abcd", "acde", 0, 1]
        ];
        ARGS.forEach(
            ([s,t,maxCost,expected]) => {
                const found = new Solve1208(s,t,maxCost).solution2()
                console.log(
                    `Leetcode[1208] s=${s} t=${t} maxCost=${maxCost} expected=${expected}, and found=${found} `, found===expected?"Passed!":"Failed!"
                )
            }
        )
    }
)()