/**
 * 2381. Shifting Letters II

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
npx ts-node ./src/app/2025/Jan/2381.ts
 */

class Solve2381 {
    public alphabets = "abcdefghijklmnopqrstuvxyz";
    public record = Object.fromEntries(Array.from(this.alphabets).map((char,i)=>[char,i]));
    public n = this.alphabets.length;
    constructor(public s:string, public shifts: [number, number, number][]){
        this.s = s; this.shifts = shifts;
    };
    next(i:number,offset:number=1){
        return this.alphabets[(i+offset)%this.n];
    };
    prev(i:number,offset:number=1){
        return this.alphabets[(this.n+i-offset)%this.n];
    };
    solution1(){
        const counter = Array.from(this.s)
        for(let [start,end,direction] of this.shifts){
            for(let i=start; i<=end; i++){
                counter[i] = !!direction ? this.next(this.record[counter[i]]) : this.prev(this.record[counter[i]])
            };
        };
        return counter.join('')
    }
}

([
    ["abc", [[0,1,0],[1,2,1],[0,2,1]]],
    [ "dztz", [[0,0,0],[1,1,1]]]
]).forEach( ([s,shifts]) => console.log(`\r\n s=${s} shifts=${shifts} Solution -> ${new Solve2381(s as string, shifts as [number,number,number][]).solution1()}`))