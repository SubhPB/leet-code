/**
 * Byimaan
 * 
 * 564. Find the Closest Palindrome
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

 CMD :- npx ts-node ./src/app/8-24/closest-palindrome-564.ts 
 */

function closestPalindrome(n: string = "123"){

    const N = Array.from(n, (i) => Number(i))


    return N
};
console.log(closestPalindrome())