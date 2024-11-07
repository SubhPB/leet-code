/**
 * Byimaan
 * 
 * 1463. Cherry Pickup II
Hard
Topics
Companies
Hint
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.

Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.

 CMD :- npx ts-node ./src/app/10-24/cherry-pick-1463.ts
 */

const grid = [
    [1,0,0,0,0,0,1],
    [2,0,0,0,0,3,0],
    [2,0,9,0,0,0,0],
    [0,3,0,5,4,0,0],
    [1,0,2,3,0,0,6]
]

function solveCherryPick(M: number[][] = grid){
    const rows = M.length, cols = M[0].length;

    const cached: {[key:string]: number} = {};

    function rec(row: number, col1: number, col2: number){
        // Base cases
        if (Math.min(col1, col2) < 0 || Math.max(col1, col2) >= cols){
            return 0
        } else if (col1 === col2) {
            return M[row][col1]
        } else if (row === rows - 1){
            // At the last row robots won't have any choice
            return M[row][col1] + M[row][col2]
        };

        if (cached[`${row}-${col1}-${col2}`]){
            return cached[`${row}-${col1}-${col2}`]
        }

        let cherries = 0;

        for(let c1 of [-1, 0, 1]){
            for(let c2 of [-1, 0, 1]){
                cherries = Math.max(
                    rec(row+1, col1 + c1, col2 + c2),
                    cherries
                )
            }
        };
        
        cherries = cherries + grid[row][col1] + grid[row][col2];
        cached[`${row}-${col1}-${col2}`] = cherries;

        return cherries
    };

    const maxCherries = rec(0, 0, cols-1);
    return maxCherries;
    
};

const product = (a1:number[], a2:number[]) => {
    return a1.map(e1 => a2.map(e2 => [e1, e2])).flat()
};

const constructMatrix = (m:number, n:number, valOrFn: ((i:number, j:number) => number) | number) => {
    const callbackFn = typeof valOrFn === 'function' ? valOrFn : () => valOrFn
    return Array.from({length: m}, () => Array.from({length: n}, callbackFn))
}

function cherryPickWithDP(M:number[][] = grid){
    const ROWS = M.length, COLS = M[0].length;
    let columnTable = constructMatrix(COLS, COLS, 0);

    for(let row in M){
        // For every row we need to calculate a column table
        let currColumnTable = constructMatrix(COLS, COLS, 0);
        
        for(let c1 = 0; c1 < COLS - 1; c1++){
            for(let c2 = c1+1; c2 < COLS; c2++){
                
                let maxCherries = 0, cherries = grid[row][c1] + grid[row][c2];
                for(let [n1, n2] of product([-1, 0, 1], [-1, 0, 1])){

                    const nc1 = c1 + n1, nc2 = c2 + n2;

                    if ([nc1, nc2].some(nc => nc < 0 || nc >= COLS)){
                        continue;
                    };
                    maxCherries = Math.max(
                        maxCherries,
                        cherries + columnTable[nc1][nc2]
                    )
                };
                currColumnTable[c1][c2] = maxCherries 
            }
        };
        columnTable = currColumnTable
    }
    for(let a of columnTable) console.log(JSON.stringify(a));
    return Math.max(...columnTable.flat())
}

console.log("Cherries ", cherryPickWithDP())
console.log(solveCherryPick(grid))