/**
 * 2145. Count the Hidden Sequences

You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
[5, 6, 3, 7] is not possible since it contains an element greater than 6.
[1, 2, 3, 4] is not possible since the differences are not correct.
Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

Example 1:

Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.
Example 2:

Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
Explanation: The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.
Example 3:

Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
Explanation: There are no possible hidden sequences. Thus, we return 0.
 

Constraints:

n == differences.length
1 <= n <= 105
-105 <= differences[i] <= 105
-105 <= lower <= upper <= 105

npx ts-node ./src/app/2025/Apr/2145.ts
 */

class Solve2145{
    constructor(public diffs:number[],public lower:number, public upper:number){
        this.diffs=diffs; this.lower=lower; this.upper=upper
    };
    solution1(differences=this.diffs, lower=this.lower, upper=this.upper){
        const n = differences.length;

        const len = upper-lower+1; //rangeLen

        const queue:[
            number/**currIndex*/,number/**lastElem */
        ][] = [];
        let res = 0;

        const lastDiff = differences[n-1];

        if (lastDiff===0){
            queue.push(
                ...(Array.from({length:len}, (_,i)=> [n-2, lower+i] as [number,number]))
            )
        } else {
            for(let lastElem=lower; lastElem<=upper; lastElem++){
                const currElem = lastElem - lastDiff;
                if (currElem>=lower&&currElem<=upper){
                    queue.push([n-2, currElem])
                }
            }
        };

        while(queue.length){
            const [i/**index */, last/**a_i+1*/] = queue.pop()!;
            if (i<0) res++;
            else {
                const currDiff = differences[i];
                const currElem = last - currDiff;
                if (currElem>=lower&&currElem<=upper){
                    queue.push([i-1, currElem])
                }
            }
        }
        return res
    };

    solution2(differences=this.diffs, lower=this.lower, upper=this.upper){
        const n = differences.length;
        let min = upper, max = upper;
        let lastElem = upper; //a_i+1

        for(let i=n-1; i>=0; i--){
            //computing a_i using -> a_i = a_i+1 - diff
            lastElem -= differences[i];
            min = Math.min(min, lastElem);
            max = Math.max(max, lastElem);
        };
        const delta = max - upper;
        max -= delta;
        min -= delta;

        if (min < lower) return 0;
        return min - lower + 1
    }
};
(
    ()=>{
        const ARGS: [number[], number, number][] = [
            // [[1,-3,4], 1, 6],
            [[3,-4,5,1,-2], -4, 5],
            [[4,-7,2], 3, 6],
        ];
        ARGS.forEach(
            ([diffs, lower, upper]) => {
                const sol = new Solve2145(diffs, lower, upper);
                console.log(`
                    Diffs=[${diffs.join(',')}]
                    lower=${lower}
                    upper=${upper}
                `);

                console.time(`s1`);
                console.log(`Sol1 = `, sol.solution1());
                console.timeEnd(`s1`)
                
                console.time(`s2`)
                console.log(`\nSol2 = `, sol.solution2());
                console.timeEnd(`s2`)
                
            }
        )
    }
)()