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

const isPalindrome = (str: string) => {
    return str === Array.from(str).reverse().join('')
};

function closestPalindrome(n: string = "123"){

    let N = Number(n);


    let i = 0;

    /** First we will go right side*/;
    while (true){
        if (isPalindrome(String(N+i))){
            break
        }
        i++;
    };

    let j = 0;
    /** Now lets go left side */
    while (true){
        if (isPalindrome(String(N-j)) || j > i){
            break
        };
        j++;
    };

    if (i < j){
        return String(N+i)
    } else {
        return String(N-j)
    };
};

console.log(closestPalindrome())