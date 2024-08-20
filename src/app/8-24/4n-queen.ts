/**
 * Byimaan
 * 
 * Given 4 x 4 chessboard, arrange four queens in a way, such that no two queens attack each other. That is, no two queens are placed in the same row, column, or diagonal
 * CMD - npx ts-node ./src/app/8-24/4n-queen.ts
 */


function placeQueen(n=4){
    const matrix = Array.from({length: 4}, () => Array.from({length: 4}, () => '.'))
    for(let r of matrix){
        console.log(r)
    }

};

console.log(placeQueen())

