/**
 * Byimaan
 * 17. Letter Combinations of a Phone Number
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

CMD npx ts-node ./src/app/8-24/phone-#-comb.ts

 */


const dict = {
    2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
} as const;   

type valuesOf<T> = T[keyof T] 

function letterCombinations (input: string){

    if (input.length < 1 || Number.isNaN(Number(input))){
        throw new Error("Invalid input value")
    };

    // 23 = ['abc', 'def']
    const nums = Array.from(input).map(num => dict[Number(num) as keyof typeof dict]) as valuesOf<typeof dict>[];

    const solve = (arr: string[], str: string) => {
        const strMultipication: string[] = [];
        for(let _str of arr){
            for(let char of str){
                strMultipication.push(_str+char)
            }
        };
        return strMultipication
    };

    let combination: string[] = Array.from(nums[0]);

    for(let i = 1; i < nums.length; i++){
        combination = solve(combination, nums[i])
    }

    return combination
};

console.log(letterCombinations('279'))
