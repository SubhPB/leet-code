/**
 * 2033. Minimum Operations to Make a Uni-Value Grid

You are given a 2D integer grid of size m x n and an integer x. In one operation,
 you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:

Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:

Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

npx ts-node ./src/app/2025/Mar/2033.ts
 */

class Solve2033{
    constructor(public grid:number[][],public x:number){
        this.grid=grid; this.x=x
    };
    solution(grid=this.grid,x=this.x){
        const m = grid.length, n=grid[0].length;
        const nums = grid.flat(1).sort((a,b) => a-b);
        let ops = 0;
        if (nums.length>1){
            const median = nums[Math.floor( (nums.length-1)/2 )];
            for(let i=0; i<m; i++){
                for(let j=0; j<n; j++){
                    const val = grid[i][j];
                    if (val===median) continue;
                    const calc =  (median - val) / (x);
                    const currOps = Math.max(-calc, calc)
                    if (!Number.isInteger(currOps)) return -1;
                    ops+=currOps
                }
            }
        }
        return ops;
    }
};

(
    ()=>{
        const ARGS: [number[][], number][] = [
            [[[2,4],[6,8]], 2],
            [[[1,5],[2,3]], 1],
            [[[1,2],[3,4]], 2]
        ];
        ARGS.forEach(([grid,x]) => console.log(`Grid=${JSON.stringify(grid)}, x = ${x} Solution = ${new Solve2033(grid,x).solution()}`))
    }
)()