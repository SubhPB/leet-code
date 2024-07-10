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

    longestCommonSubstring(x = "abcdxyz", y = "xyzabcd"){
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

    printLongestCommonSubstring(x = 'pqabcxy', y = 'xyzabcp'){

        // So first we will find the length then we will go or actual substring

        const m = x.length, n = y.length, matrix = Array.from({length: m+1}, () => Array.from({length: n+1}, () => 0));
        // When the length of either array is zero then our answer would be zero so that will be our base case.
        let maxLength = 0, iAt = 0;

        for(let i = 1; i <= m; i++){
            for(let j = 1; j <= n; j++){

                // matched
                if (x[i-1] === y[j-1]){
                    matrix[i][j] = matrix[i-1][j-1] + 1
                } else {
                    // not matched
                    matrix[i][j] = 0
                };

                if (matrix[i][j] > maxLength){
                    maxLength = matrix[i][j]
                    iAt = i
                }
            }
        };

        return x.substring(iAt - maxLength, iAt)
    }

    printLongestCommonsubsequence(x = 'acbcf', y = 'abcdaf'){
        /* we will print the longest common substring with the following strategy :-
        *   1. find the matrix where its each slot represents the M[i][j] = length of longest common subsequence
        *   2. Then we will track back over the matrix to find out the actual string
        */

        const m = x.length, n = y.length, matrix = Array.from({length: m+1}, () => Array.from({length: n+1}, () => 0));

        for (let i = 1; i <= m; i++){
            for(let j = 1; j <= n; j++){

                if (x[i-1] === y[j-1]){
                    matrix[i][j] = matrix[i-1][j-1] + 1
                } else {
                    matrix[i][j] = Math.max(matrix[i-1][j], matrix[i][j-1])
                }

            }
        }
        

        let i = m, j = n, maxLength = matrix[m][n],subStr = '';

        while (i > 0 && j > 0 && subStr.length !== maxLength){
            if (x[i-1] === y[j-1]){
                subStr = x[i-1] + subStr
                i--; 
                j--;
            } else if (matrix[i-1][j] > matrix[i][j-1]){
                i--;
            } else {
                j--;
            }
        };
        return subStr
    }

};

const lcs = new LCS();
console.log(lcs.printLongestCommonsubsequence())

export { LCS }