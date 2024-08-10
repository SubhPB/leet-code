// Byimaan

/**
 * 72. Edit Distance
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

    You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
    

    Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
    Example 2:

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')

    CMD = npx ts-node ./src/app/8-24/edit-distance-72.ts
 */


class EditDistance {
    constructor (public word1 = "horse", public word2 = "ros"){
        this.word1 = word1;
        this.word2 = word2
    }
    recursion(word1=this.word1, word2=this.word2){

        const solve = (str1: string, str2: string): number => {
            if (str1.length === 0){
                return str2.length
            };

            if (str2.length === 0){
                return str1.length
            };

            if (str1[0] === str2[0]){
                return solve(str1.slice(1), str2.slice(2))
            } else {
                return 1 + Math.min(
                    solve(str1.slice(1), str2.slice(1)),
                    solve(str1, str2.slice(1)),
                    solve(str1.slice(1), str2)
                )
            }
        };

        return solve(word1, word2)
    }
};

const editDistance = new EditDistance();
console.log(editDistance.recursion())