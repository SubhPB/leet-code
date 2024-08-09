// Byimaan

/**
 * Problem Statement: "Hard" - "Palindrome Partitioning II"
    Description:
    Given a string s, you need to partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of the string.

    Input: s = "abacabad"
    Output: 1

    CMD - npx ts-node ./src/app/8-24/min-palindrome-partition.ts
 */

// recursion approach
class Recursion {
    constructor (public s: string) {
        this.s = s
    };


    findLongestPalindromeSubString(s=this.s){
        // recusion approach

        const recursion = (str : string) => {
            if (str.length <= 2){
                return str
            };

            let median = str.length / 2;
            if (str.slice(0, Math.ceil(median)) === Array.from(str.slice(Math.floor(median))).reverse().join('')){
                return str
            };

            const choice1 = recursion(str.slice(1)) as string, 
            choice2 = recursion(str.slice(0, str.length - 1)) as string;

            if (choice1.length > choice2.length){
                return choice1
            };

            return choice2
        };

        return recursion(s)
    };

    findMinPalindromePartition(s=this.s){

        const recursion = (str: string): number => {
            if (str.length <= 2){
                return 0
            };

            const longestPalindromeSubstring = this.findLongestPalindromeSubString(str);
            if (longestPalindromeSubstring.length === str.length){
                return 0
            };

            const index = str.indexOf(longestPalindromeSubstring);

            if (index < 0){
                throw new Error("There is something wrong in the logic of this.findLongestPalindromeSubString")
            };

            const before = s.slice(0, index), after = s.slice(index+longestPalindromeSubstring.length);

            return 1 + recursion(before) as number + recursion(after) as number
        };
        return recursion(s)
    }
};

// dp approach
class DP {
    constructor (public s: string){
        this.s = s
    };

    findLongestPalindromeSubString(s=this.s){
        const matrix = Array.from({length: s.length+1},() => Array.from({length: s.length+1}, () => 0));
        const reversedS = Array.from(s).reverse().join('')

        let palindromeStr = '';
        for(let i = 1; i <= s.length; i++){
            for(let j = 1; j <= s.length; j++){
                if (s[i-1] === reversedS[j-1]){
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    if (matrix[i][j] > palindromeStr.length){
                        palindromeStr = s.slice(i-matrix[i][j],i)
                    }
                } else {
                    matrix[i][j] = 0
                }
            }
        };
        return palindromeStr
    };
    findMinPalindromePartition(s=this.s){
        
        let partitions = 0
        const stack = [s];
        
        while (stack.length !== 0){
            const str = stack.pop() as string;

            if (str.length > 2){
                const palindrome = this.findLongestPalindromeSubString(str);
                const index = str.indexOf(palindrome);

                if (palindrome.length === 1){
                    partitions += (str.length - 1);
                    continue
                };

                if (palindrome.length === str.length){
                    continue
                };

                if (index > 0){
                  stack.push(s.slice(0, index))  
                };
                if (index + palindrome.length < str.length){
                    stack.push(s.slice(index+palindrome.length))
                };
                partitions += 1
            }
        }

        return partitions
    }
}

class Palindrome {
    public recursion : Recursion;
    public dp : DP;
    constructor (public s: string) {
        this.s = s
        this.recursion = new Recursion(s)
        this.dp = new DP(s)
    };


};    


const palindrome = new Palindrome("abacabad");
console.log(palindrome.dp.findMinPalindromePartition())

