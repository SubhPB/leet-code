// Byimaan

/**
 * 
 *  Input : N=10
    Coins : 1, 5, 10
    Output : 4
    Explanation: 
    1 way: 
    1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 cents.
    2 way: 
    1 + 1 + 1 + 1 + 1 + 5 = 10 cents.
    3 way: 
    5 + 5 = 10 cents.
    4 way: 
    10 cents = 10 cents.
    CMD npx ts-node ./src/app/7-24/coin-change.ts
 */

const coins = [1, 5, 10], m = coins.length, n = 10

const coinChange = () => {
    const matrix = Array.from({length: m+1}, () => [1, ...Array(n).fill(0)]);
    const print = () => {
        for(let a of matrix){
            console.log(JSON.stringify(a))
        }
    };

    print()
    for(let i = 1; i <= m; i++){
        for (let j = 1; j <= n; j++){
            if (coins[i-1] > j){
                matrix[i][j] = matrix[i-1][j]
            } else {
                matrix[i][j] = matrix[i][j-coins[i-1]] + matrix[i-1][j];
            }
        }
    };
    print()
};

coinChange();