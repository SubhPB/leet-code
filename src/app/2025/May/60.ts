/**
 * 
60. Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

 npx ts-node ./src/app/2025/May/60.ts
 */

class Solve60{
    constructor(public n:number, public k:number){
        this.n=n; this.k=k;
    };
    solution(n=this.n,k=this.k){ //O(n) time-complexity 
        const res = Array(n).fill(-1);
        const ints = Array.from({length:n+1},(_,i)=>i>0?i:1);

        const delInt = (i:number) => {
            ints[i] = ints[ints.length-1];
            ints.length -= 1;
            ints.sort((a,b)=>a-b);
        }

        let perms = ints.reduce((acc, int) => acc*int, 1);
        let group = 0;
        while(group<n){
            /**
            * Perms refers: How many children does each group/sub-group has? 
            * e.g. if there are 120 possible ways to arrange then there are 120/n = 120/5 => 24
            *      means each group has 24 children/sub-possible ways
            */
            perms = perms / (n-group); // perms equals groupSize
            
            /**
            * "k" should be at-least 1 because ints[0] is a dummy value.
            * If it is found to be 0 Then it points outs to the very-last permutation possible at current subGroup
            * (n-group)*perms will give the last kth value.
            */
            if (k===0) k = (n - group)*perms;
    
            const intAt = Math.ceil(k/perms);
            res[group] = ints[intAt]; //Sub-group leader found!
    
            delInt(intAt); //An int can't be reused, better to delete it!
    
            k %= perms; 
            group+=1;
        }

        return res.join('');
    }
};

(
    ()=>{
        const ARGS = [
            [3,3], [4,9], [3,1],
            [5,99]
        ];
        ARGS.forEach(
            ([n,k]) => {
                const sol = new Solve60(n,k);
                console.log(`N=${n} and K=${k} Permutation=${sol.solution()}`)
            }
        )
    }
)()