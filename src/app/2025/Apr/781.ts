/**
 * 781. Rabbits in Forest

There is a forest with an unknown number of rabbits.
 We asked n rabbits "How many rabbits have the same color as you?"
  and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11

Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000

npx ts-node ./src/app/2025/Apr/781.ts
 */

class Solve781{
    constructor(public answers:number[]){
        this.answers = answers;
    };
    solution1(answers=this.answers){
        const n = answers.length;
        const sort = [...answers].sort((a, b) => a-b);

        let i=0, res = 0;
        while(i<n){
            const ans = sort[i];
            let group = 1;
            while(i+1<n && group<=ans && sort[i+1]===ans){
                group++;
                i++;
            };
            res += ans+1;
            i++;
        };
        return res;
    }
};

(
    ()=>{
        const ARGS = [
            [1,1,2],
            [10,10,10],
            [1,1,1,1,1]
        ];
        ARGS.forEach(
            ans => {
                const sol = new Solve781(ans);
                console.log(`Answers=[${ans.join(', ')}] Min-population=${sol.solution1()}`)
            }
        )
    }
)()