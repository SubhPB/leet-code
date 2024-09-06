/**
 * Byimaan
 * 
    Return the shortest palindrome you can find by performing this transformation.

    Example 1:

    Input: s = "aacecaaa"
    Output: "aaacecaaa"
    Example 2:

    Input: s = "abcd"
    Output: "dcbabcd"

    CMD :- npx ts-node ./src/app/9-24/shortest-palindrome-214.ts
 */

function shortestPalindrome(s = "aacecaaa"){
    /**
     * what could be worst case palindrome scenrio for solution --> aaacecaa + aacecaaa
     */

    const isPalindrome = (str:string) => {
        return str === Array.from(str).reverse().join('')
    }

    const rec = (frontStr:string) => {
        const newStr = frontStr + s;
        if (isPalindrome(newStr)){
            return newStr
        } else {
            const modifiedFrontStr = s[s.length - 1 - frontStr.length] + frontStr;
            return rec(modifiedFrontStr)
        }
    };
    return rec('')
};
console.log(shortestPalindrome())