
class Contest491 { //#3857-59

    dp:number[]; // cache #3857
    constructor(){

        /**3857*/
        const inf = 1e9; this.dp = Array(501).fill(inf);
        this.dp[1]=0
        for(let x=1; x<=500; x++){
            for(let a=1; a<=Math.ceil(x/2); a++){
                this.dp[x]=Math.min(this.dp[x],a*(x-a)+this.dp[a]+this.dp[x-a])
            }
        };
    }

    /**
     * 3857. Minimum Cost to Split into Ones
        You are given an integer n.
        In one operation, you may split an integer x into two positive integers a and b such that a + b = x.
        The cost of this operation is a * b.
        Return an integer denoting the minimum total cost required to split the integer n into n ones.

        Example 1:
        Input: n = 3
        Output: 3
        Thus, the minimum total cost is 2 + 1 = 3.

        Constraints:
        1 <= n <= 500
     */
    minCost(n: number): number { //O(1)
        return this.dp[n]
    };
}