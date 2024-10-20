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


function cherryPick(M: number[][] = grid){

    let cherries = 0;

    const isValidMove = (r:number, c:number) => {
        return r < M.length && r >= 0
            &&  c < M[0].length && c >= 0
    }

    const getPossibleMoves = (r:number, c: number) => {
        const left = [r+1, c-1],
            right = [r+1, c+1],
            straight = [r+1, c];
        //@ts-ignore    
        return [left, straight, right].filter(dir => isValidMove(...dir))
    }

    /** computation */

    const rec = (robo1 : number[], robo2 : number[], cherryCount : number, level : number)  => {
        if (level === M.length - 1){
            if (cherryCount === 30){
                console.log("Args when reached 30 : ", robo1, robo2, cherryCount, level);
                for(let a of M){
                    console.log(a)
                }
            };
            if (cherryCount > cherries) cherries = cherryCount;
            return 
        };

        //@ts-ignore
        const possibleMovesForRobo1 = getPossibleMoves(...robo1),
            //@ts-ignore
            possibleMovesForRobo2 = getPossibleMoves(...robo2);

        
        for(let r1Move of possibleMovesForRobo1){
            for (let r2Move of possibleMovesForRobo2){
                const slot1 = M[r1Move[0]][r1Move[1]],
                    slot2 =  M[r2Move[0]][r2Move[1]];
                const cherriesCollected = slot1 + slot2;

                M[r1Move[0]][r1Move[1]] = 0;
                M[r2Move[0]][r2Move[1]] = 0;
                rec(r1Move, r2Move, cherryCount + cherriesCollected, level+1);
                M[r1Move[0]][r1Move[1]] = slot1;
                M[r2Move[0]][r2Move[1]] = slot2
            }
        }
    };

    const r1StartPoint = [-1, 0], 
        r2StartPoint = [-1, M[0].length - 1];
    
    rec(
        r1StartPoint,
        r2StartPoint,
        0,
        -1
    )

    return cherries
};

console.log(cherryPick(grid))