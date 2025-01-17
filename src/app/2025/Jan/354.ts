/**\
 * 354. Russian Doll Envelopes
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

CMD npx ts-node ./src/app/2025/Jan/354.ts
 */

class Solve354{
    constructor(public envelops:number[][]){
        this.envelops = envelops.sort(
            //ascending order
            ([w1,h1],[w2,h2]) => w1*h1 - w2*h2
        );
    };
    solution1(){
        /**
         * This problem is basically a subproblem of longest increasing subsequence 
         */
        const n = this.envelops.length;
        const dp :number[] = []; /**
         * dp[i] represents minimum ending value possible of a longest increasing subsequence at a particular length means i+1.
         */

        for(let i=0; i<n; i++){
            let left = 0, right = dp.length;
            while(left<right){
                const mid = Math.floor(
                    (left+right)/2
                ), [
                    w1,h1
                ] = this.envelops[i], [
                    w2,h2
                ] = this.envelops[dp[mid]];
                
                if (w1<w2&&h1<h2){
                    right=mid
                } else {
                    left=mid+1
                }
            };
            if (left<dp.length){
                dp[left] = i
            } else dp.push(left)
        };
        console.log(`dp=${dp}`)
        return dp.length
    }
};

(
    ()=>{
        const ARGS = [
            [[5,4],[6,4],[6,7],[2,3]],
        ];
        ARGS.forEach(
            envs => {
                console.log(`\n Envelops = ${JSON.stringify(envs)}, LIS -> ${new Solve354(envs).solution1()}`)
            }
        )
    }
)()