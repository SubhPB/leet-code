// Byimaan

/**
 * LCS class will solve all the problems which follows the pattern of longest common subsequence.
 *  - Each method will be dedicated to one specfic problem
 *  - CMD npx ts-node ./src/app/7-24/lcs.ts
 */

class LCS {

    print(matrix: number[][]){
        for(let a of matrix){
            console.log(JSON.stringify(a))
        }
    }

    longestCommonSubsequence(x = "abcdxyz", y = "xyzabcd"){ 
        /**
         * Input : X = “abcdxyz”, y = “xyzabcd” 
            Output : 4 
            Explanation:
            The longest common subsequence is “abcd” and is of length 4
        */

        const m = x.length, n = y.length, matrix: number[][] = Array.from({length: m+1}, () => Array.from({length: n+1}, () => 0))


        for (let i = 1; i <= m; i++){
            for (let j = 1; j <= n; j++){
                if (x[i-1] === y[j-1]){
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                } else {
                    matrix[i][j] = Math.max(matrix[i-1][j] ,matrix[i][j-1])
                }
            }
        };

        this.print(matrix)

        return matrix[m][n]
    }

    longestCommonSubString(x = "abcdxyz", y = "xyzabcd"){
        /**
         * Input : X = “abcdxyz”, y = “xyzabcd” 
            Output : 4 
            Explanation:
            The longest common subsequence is “abcd” and is of length 4
        */

        const m = x.length, n = y.length, matrix: number[][] = Array.from({length: m+1}, () => Array.from({length: n+1}, () => 0))
        let maxLength = 0

        for (let i = 1; i <= m; i++){
            for (let j = 1; j <= n; j++){
                if (x[i-1] === y[j-1]){
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                    maxLength = Math.max(maxLength, matrix[i][j])
                } else {
                    matrix[i][j] = 0
                }
            }
        }

        this.print(matrix)

        return maxLength
    }

};

const lcs = new LCS();
console.log(lcs.longestCommonSubsequence())