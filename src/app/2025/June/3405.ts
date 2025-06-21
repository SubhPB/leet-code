/**
 * 3405. Count the Number of Arrays with K Matching Adjacent Elements

    You are given three integers n, m, k. A good array arr of size n is defined as follows:

    Each element in arr is in the inclusive range [1, m].
    Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
    Return the number of good arrays that can be formed.

    Since the answer may be very large, return it modulo 109 + 7.

    

    Example 1:

    Input: n = 3, m = 2, k = 1

    Output: 4

    Explanation:

    There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
    Hence, the answer is 4.
    Example 2:

    Input: n = 4, m = 2, k = 2

    Output: 6

    Explanation:

    The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
    Hence, the answer is 6.
    Example 3:

    Input: n = 5, m = 2, k = 0

    Output: 2

    Explanation:

    The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
    

    Constraints:

    1 <= n <= 10^5
    1 <= m <= 10^5
    0 <= k <= n - 1
    npx ts-node ./src/app/2025/June/3405.ts
 */

class Solution3405 {
    constructor(public n:number, public m:number, public k:number){
        this.n=n; this.m=m; this.k=k;
    };

    countGoodArrays(n=this.n, m=this.m, k=this.k){
        const M = 1e9+7;
        const MUL = (x:number,y:number) => (x%M * y%M)%M;

        const binaryExp = (base:number, exp:number) => {
            let res = 1;
            while(exp>0){
                if (exp&1) res = MUL(res, base);
                base = MUL(base, base);
                exp=Math.floor(exp/2);
            }
            return res;
        }

        const perm = Array(1e5+1).fill(1)
        const inverse_perm = Array(1e5+1).fill(1)
        for(let i=1; i<=1e5; i+=1){
            perm[i] = MUL(perm[i-1], i);
            inverse_perm[i] = binaryExp(perm[i], M-2)%M;
        };

        const comb = (N:number,K:number) => MUL(
            perm[N],
            MUL(
                inverse_perm[N-K],
                inverse_perm[K]
            )
        );
        
        const nEqlPairs = n-1-k, slots = nEqlPairs+1;
        let res = MUL(
            comb(n-1, slots-1),
            MUL(
                m,
                binaryExp(m-1, slots-1)
            )
        )
        return res;
    };
};

(
    ()=>{
        const ARGS = [
            [ 3, 2, 1],
            [4, 2, 2],
            [5, 2, 0]
        ];

        ARGS.forEach(([n,m,k]) => {
            console.log(`n=${n} m=${m} k=${k} ans=${new Solution3405(n,m,k).countGoodArrays()}`)
        })
    }
)()