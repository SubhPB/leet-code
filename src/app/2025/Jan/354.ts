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
        console.log(`Before sort `, this.envelops);
        this.envelops = this.sort();
        console.log(`After sort `, this.envelops)
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
                
                if (w1<=w2&&h1<=h2){
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
    };
    sort(){
        //Goal here is to sort according envelop dimension, not only according area but equally considering width and height.
        //We can'tv rely on area e.f (i) 2*3=6 (ii) 8*1=8 even though area is more but can't put the first envelop as whole.
        const n = this.envelops.length;
        const mergeSort = (
            envs:number[]=Array.from({length:n},(_,i)=>i) //Will use indexes to calc sorting algorithm
        ) => {
            const len = envs.length;
            if (len<=1) return envs;

            const mid = Math.floor( len/2 );
            const sortedEnvs: number[] = [];

            const s1 = mergeSort(envs.slice(0, mid)),
                s2 = mergeSort(envs.slice(mid, len));

            let i=0, j=0;

            while(i<mid&&j<(len-mid)){
                /* Need to sort according dimension  */
                const [w1,h1] = this.envelops[s1[i]],
                    [w2,h2] = this.envelops[s2[j]];
                if(w1<w2&&h1<h2){
                    sortedEnvs.push(s1[i]); i++;
                } else {
                    sortedEnvs.push(s2[j]); j++;
                }
            };

            while(i<mid){
                sortedEnvs.push(s1[i]);
                i++
            }
            while(j<(len-mid)){
                sortedEnvs.push(s2[j]);
                j++
            }


            return sortedEnvs;
        };
        const sortedEnvs = mergeSort();
        return sortedEnvs.map(envIndex=>this.envelops[envIndex])
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