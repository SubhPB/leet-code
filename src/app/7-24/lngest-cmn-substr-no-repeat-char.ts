// Byimaan

/**
 * 
 * Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

For example:

Input: "abcabcbb"
Output: 3 (The answer is "abc", with the length of 3
 * 
 * CMD :- npx ts-node ./src/app/7-24/lngest-cmn-substr-no-repeat-char.ts
 */

function findLongestSubStringWithoutRepeatingChars(str="abcabcbb"){

    let lngest = '';

    for(let i = 0; i < str.length - 1; i++){
        let tempStr = str[i]
        for(let j = i+1; j < str.length; j++){
            if (!tempStr.includes(str[j])){
                tempStr += str[j]
            } else {
                break;
            }
        };
        if (tempStr.length > lngest.length){
            lngest = tempStr
        }
    };
    return lngest;
};

console.log(findLongestSubStringWithoutRepeatingChars())