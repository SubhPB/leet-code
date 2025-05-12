/**
 * 3546. Equal Sum Grid Partition I

You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:

A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105


 npx ts-node ./src/app/2025/May/3546.ts
 */

class Solve3346{
    constructor(public grid:number[][]){
        this.grid=grid
    };
    solution(grid=this.grid){
        const m = grid.length, n = grid[0].length;

        // :To keep sum record of [C0, C1, ..., CN] and [R0, R1, ..., RN]
        const colSum = Array(n+1).fill(0);
        const rowSum = Array(m+1).fill(0);

        for(let r=0; r<m; r++){
            rowSum[r+1] += rowSum[r]; // Curr row/col should also keeps the sum of prevRows/prevCols
            for(let c=0; c<n; c++){
                rowSum[r+1] += grid[r][c];
                colSum[c+1] += grid[r][c];
            };
        };

        const Sn = rowSum[m];
        if ((Sn&1)===0){
            /**
             * Let's see if we can find solution by cutting rows
             */
            for(let row=1; row<m; row++) {
                if (rowSum[row]===Sn-rowSum[row]) return true
            };
            
            //Maintaining prevColSum, was not maintained in nested loop
            for(let col=1; col<=n; col++) colSum[col] += colSum[col-1];
            //Let's check if can find answer by cutting cols
            for(let col=1; col<n; col++){
                if (colSum[col]===Sn-colSum[col]) return true;
            };
        };

        return false;
    }
};

(
    ()=>{
        const ARGS = [
            [[1,4],[2,3]],
            [[1,3],[2,4]],
            [[54756], [54756]]
        ];

        ARGS.forEach(
            grid => {
                console.log('\n Grid:');
                for(let row of grid){
                    console.log(`| ` + row.join(' | ') + ` |`)
                };
                console.log(`Partition possible: ${new Solve3346(grid).solution()}`)
            }
        )
    }
)()