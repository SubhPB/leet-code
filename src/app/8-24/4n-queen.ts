/**
 * Byimaan
 * 
 * Given 4 x 4 chessboard, arrange four queens in a way, such that no two queens attack each other. That is, no two queens are placed in the same row, column, or diagonal
 * CMD - npx ts-node ./src/app/8-24/4n-queen.ts
 */

class Queen {
    constructor(public x: number, public y:number){
        this.x = x;
        this.y = y;
    };

    /** x and y is the location of other chess piece */
    isUnderAttack(x:number, y: number){
        const verticalOrHorizontalLineUnderAttck = this.x === x || this.y === y
        const diagonalsUnderAttack = /** bottomLeftToTopright || topLeftToBottomRight */ this.x + this.y === x + y || this.x - this.y === x - y
        return verticalOrHorizontalLineUnderAttck || diagonalsUnderAttack
    }

}

function placeQueen(n=4){
    const matrix = Array.from({length: 4}, () => Array.from({length: 4}, () => ' '));
    
    const sols:number[][][] = []

    const backTrack = (row: number, paths: number[][]) => {
        if (paths.length === n){
            console.log("HELO!")
            sols.push(paths)
            return;
        };
        
        if (row >= n){
            return
        }
        
        for (let col = 0; col < n; col++){
            /** x will be col and y will be row because col moves in horizonal fashion and row moves in vertical fashion  */
            const isSafe = paths.every(([x, y] )=> !(new Queen(col, row).isUnderAttack(y, x)));
            if (isSafe){
                backTrack(row+1, [...paths, [row, col]])
            }
        }
    };
    backTrack(0, [])
    return sols
};

console.log(placeQueen())

