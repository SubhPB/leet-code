/**
 * 
790. Domino and Tromino Tiling

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.


Example 1:
Input: n = 3
Output: 5

Explanation: The five different ways are show above.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 1000

npx ts-node ./src/app/2025/May/790.ts
 */

class Solve790{
    constructor(public n:number){
        this.n=n;
    };
    memoSolution(n=this.n){
        const MOD = 1e9 + 7;
        const dp = Array.from({length:n+1}, 
           () => Array(n+1).fill(-1)
        );
        dp[0][0] = 1; 

        const ops = (r1:number, r2:number)=> {
            const H = [r1-2,r2-2];
            const H1 = [r1-2,r2];
            const H2 = [r1,r2-2];
            const V = [r1-1,r2-1];
            const L1 = [r1-1,r2-2]; // |_
            const L2 = [r1-2,r2-1]; // |^
            const L3 = [r1-1,r2-2]; // _|
            const L4 = [r1-2,r2-1]; // ^|

            const diff = r2-r1;
            if (diff===0){
                return [H,V,L3,L4]
            } else if (diff>0){
                return [L1,H2]
            } else {
                return [L2,H1]
            }
        }

        const fn = (r1:number, r2:number) => {
            if ([r1,r2].every(r=>r>=0)){
                if (dp[r1][r2]!==-1) return dp[r1][r2];
            
                let ways = 0;
                for(let [nxtR1,nxtR2] of ops(r1,r2)){
                    ways += fn(nxtR1, nxtR2);
                    ways %= MOD
                };
                dp[r1][r2] = ways;
                return ways
            } else {
                return 0
            }
        };

        fn(n,n)
        return dp[n][n]
    };
    dpSolution(n=this.n){
        const MOD = 1e9+7;
        const dp = Array.from(
            {length:n+1}, () => Array(n+1).fill(0)
        );

        const ops = (r1:number,r2:number) =>  {
            const diff = r2-r1;
            if (diff===0){
                return [
                    [r1-2, r2-2], //H
                    [r1-1,r2-1], //V
                    [r1-2, r2-1], //^^|
                    [r1-1,r2-2], //_|
                ]
            } else if (diff>0){
                return [
                    [r1-1,r2-2],
                    [r1,r2-2]
                ]
            } else {
                return [
                    [r1-2,r2-1],
                    [r1-2, r2]
                ]
            }
        };

        dp[0][0]=1;

        for(let r1=1; r1<=n; r1+=1){
            let r2=r1-1;
            
            while(r2<=Math.min(r1+1, n)){
                let ways = 0;
                for(let [nxtR1,nxtR2] of ops(r1,r2)){
                    if ([nxtR1,nxtR2].every(r=>r>=0)){
                        ways += dp[nxtR1][nxtR2];
                        ways %= MOD;
                    }
                };
                dp[r1][r2]=ways;
                r2+=1;
            };
        };
        return dp[n][n]
    }
};


(
    ()=>{
        const ARGS = [
            3,1
        ];
        ARGS.forEach(
            n => {
                const sol = new Solve790(n);
                console.log(`N=${n} MemoSol=${sol.memoSolution()} DpSol=${sol.dpSolution()}`)
            }
        )
    }
)()

