// Byimaan

/**
 * Problem Statement: "Hard" - "Palindrome Partitioning II"
    Description:
    Given a string s, you need to partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of the string.

    Input: s = "abacabad"
    Output: 1

    CMD - npx ts-node ./src/app/8-24/min-palindrome-partition.ts
 */

class Palindrome {
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


const palindrome = new Palindrome("abacabad");

console.log(palindrome.findMinPalindromePartition())