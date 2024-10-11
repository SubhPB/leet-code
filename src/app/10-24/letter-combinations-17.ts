/**
 * 17. Letter Combinations of a Phone Number
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 CMD :- npx ts-node ./src/app/10-24/letter-combinations-17.ts
 */

const digitToChar = {
    '0': '',
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
};


function letterCombinations17(digits: string): string[] {

    if (![...digits].every(digit => Object.keys(digitToChar).includes(digit))){
        return []
    };

    function solveByRec(_digits: string): string[] {
        if (!_digits){
            return ['']
        };

        const digit = _digits[0] as keyof (typeof digitToChar);
        const curr = [...digitToChar[digit]];
        const next = [...solveByRec(_digits.slice(1))];

        
        const combinations:string[] = [];
        
        for(let a of curr){
            for (let b of next){
                combinations.push(a+b)
            }
        };
        return combinations
    }
    
    return solveByRec(digits)
};

console.log(" #### LeetCode 17 ####")
console.log(letterCombinations17("23"))
