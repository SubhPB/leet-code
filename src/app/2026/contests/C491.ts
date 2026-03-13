
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

    /**
     * 3858. Minimum Bitwise OR From Grid
        You are given a 2D integer array grid of size m x n.
        You must select exactly one integer from each row of the grid.
        Return an integer denoting the minimum possible bitwise OR of the selected integers from each row.

        Example 1:
        Input: grid = [[1,5],[2,4]]
        Output: 3
        Explanation:
        Choose 1 from the first row and 2 from the second row.
        The bitwise OR of 1 | 2 = 3​​​​​​​, which is the minimum possible.
        
        Constraints:
        1 <= m == grid.length <= 10^5
        1 <= n == grid[i].length <= 10^5
        m * n <= 10^5
        1 <= grid[i][j] <= 10^5
    */
    minimumOR(grid: number[][]): number {
        /**
         * Rough Idea:
         * max_bit_length_possible : x = 1 + log2(10**5)//1
         * mask = 1<<(x)-1
         * for each bit starting left to right, for each row check if atleast 1x bit fits inside the temp mask,
         * if any row it fails then conclude that we can't remove the bit else it is removable
         */
        return -1;  
    };
}