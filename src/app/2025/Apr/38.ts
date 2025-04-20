/**
 * 38. Count and Say
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.


Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

npx ts-node ./src/app/2025/Apr/38.ts
 */

class Solve38{
    constructor(public i:number){
        this.i=i;
    };
    solution1(i=this.i){

        const rle = (str:string) => {
            let lastChar = str[0], count = 0;
            let res = ''
            for(let char of str){
                if (char !== lastChar){
                    res += `${count}${lastChar}`
                    lastChar = char;
                    count = 0
                };
                count++
            };
            res += `${count}${lastChar}`
            return res;
        }
        const countAndSay = (a:number): string => {
            if (a===1) return "1";
            return rle( 
                countAndSay(a-1)
            )
        };

        return countAndSay(i)
    };
};

(
    ()=>{
        const ARGS = Array.from({length:20}, (_,i) => i+1);

        ARGS.forEach(
            n => {
                const sol = new Solve38(n);
                console.log(`N = ${n}  Encoded-value = ${sol.solution1().length}`)
            }
        )
    }
)()