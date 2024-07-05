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

class CoinChange {

    print(matrix: number[][]){
        for(let a of matrix){
            console.log(JSON.stringify(a))
        }
    }

    totalNoOfWays(coins: number[]= [1, 5, 10], n: number = 10 ){
        /**
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
        const m = coins.length;
        const matrix = Array.from({length: m+1}, () => [1, ...Array(n).fill(0)]);

        for(let i = 1; i <= m; i++){
            for (let j = 1; j <= n; j++){
                if (coins[i-1] > j){
                    matrix[i][j] = matrix[i-1][j]
                } else {
                    matrix[i][j] = matrix[i][j-coins[i-1]] + matrix[i-1][j];
                }
            }
        };

        return matrix[m][n]
    };

    minCoins(coins: number[]=[1, 2, 5], amount: number=11){
        /**
         * Input: coins = [1,2,5], amount = 11
            Output: 3
            Explanation: 11 = 5 + 5 + 1
         */

        const m = coins.length, n = amount;

        const matrix = function ieef(){
            const M: (number)[][] = []
            for(let i = 0; i <= m; i++){
                M.push([])
                for (let j = 0; j <= n; j++){
                    if ( i === 0 ){
                        M[i].push(Infinity)
                    }else if (j === 0){
                        M[i].push(0)
                    } else if (i === 1){
                        if (coins[i-1] > j){
                            M[i].push(0)
                        } else {
                            M[i].push(M[i][j-coins[i-1]]+1) 
                        }
                    } else {
                        M[i].push(Infinity)
                    }
                }
            };
            return M as number [][]
        }();

        this.print(matrix)
        console.log()

        for(let i = 2; i <= m; i++){
            for (let j = 1; j <= n; j++){
                if (coins[i-1] > j){
                    matrix[i][j] = matrix[i-1][j]
                } else {
                    matrix[i][j] = Math.min(matrix[i][j-coins[i-1]] + 1, matrix[i-1][j])
                }
            }
        };

        this.print(matrix)
    };


};

const coinChange = new CoinChange()
console.log(coinChange.minCoins())