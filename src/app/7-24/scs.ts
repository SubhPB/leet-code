// Byimaan

/**
 * Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.
 * 
 * Input:   str1 = "geek",  str2 = "eke"
    Output: 5
    Explanation: 
    String "geeke" has both string "geek" 
    and "eke" as subsequences.

    Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
    Output:  9
    Explanation: 
    String "AGXGTXAYB" has both string 
    "AGGTAB" and "GXTXAYB" as subsequences

    CMD npx ts-node ./src/app/7-24/scs.ts

 */

import { LCS } from "./lcs";

class SCS {

   lcs : LCS = new LCS()

   findShortestSuperSequence(x = "geek",  y = "eke"){

      // appproach: find the longest common subsequence of x and y
      // then subtract with the sum of length of x and y
      const lcs = this.lcs.longestCommonSubsequence(x, y);

      return x.length + y.length - lcs

   };

   printShortestSuperSequence(x = "AGGTAB",  y= "GXTXAYB"){
      // Approach :-
      //    find the matrix of longest common subsequence and then track back the values to figure out the 
      //    actual shortest supersequence
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

      const scsLength = x.length + y.length -  matrix[m][n] 

      let i = m, j = n, scs = '';

      while ((i > 0 || j > 0) && scs.length !== scsLength){

         if (i === 0 && j !== 0){
            console.log(`scs when i = 0 and j = ${j}`, scs)
            scs = y.substring(0,j) + scs;
            break
         } else if (j === 0 && i !== 0){
            console.log(`scs when i = ${i} and j = ${j}`, scs)
            scs = x.substring(0, i) + scs
            break
         }

         if (x[i-1] === y[j-1]){
            scs = x[i-1] + scs;
            i--;
            j--;
         } else {
            if (matrix[i-1][j] > matrix[i][j-1]){
               scs = x[i-1] + scs;
               i--;
            } else {
               scs = y[j-1] + scs;
               j--;
            }
         }
      }

      return scs
   };
};

const scs = new SCS();
console.log('SCS = ', scs.printShortestSuperSequence())