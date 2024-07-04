// Byimaan

/**
 * 
 * Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

    length   | 1   2   3   4   5   6   7   8  
    --------------------------------------------
    price    | 1   5   8   9  10  17  17  20

    output = 22 
 * CMD npx ts-node ./src/app/7-24/cutting-rod.ts
 */

const _length = [1, 2, 3, 4, 5, 6, 7, 8], price = [1, 5, 8, 9, 10, 17, 17, 20];

const findMaxPrice = () => {
    const [m, n] = [_length.length, _length.length]
    // const matrix: number[][] = Array(m).fill(Array.from({length: n}, (v, i) => 0));
    const matrix = Array.from({length: m+1}, () => Array.from({length: n+1}, () => 0));

    const print = () => {
        for (let a of matrix){
            console.log(JSON.stringify(a));
        }
    };

    print()
    console.log('')

    for(let i = 1; i <= m; i++){
        for(let j = 1; j <= n; j++){

            if (i > j){
                matrix[i][j] = matrix[i-1][j]
            } else {
                matrix[i][j] = Math.max(matrix[i-1][j], matrix[i][j-i] + price[i-1]);
            }

        }
    }
    print()
};

findMaxPrice()