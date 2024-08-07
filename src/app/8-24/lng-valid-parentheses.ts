// BYIMAAN

/**
 * 32. Longest Valid Parentheses
Hard
Topics
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

CMD - npx ts-node ./src/app/8-24/lng-valid-parentheses.ts
 */


function findLongestParentheses(s = ")(()()))"){
    const stack: string[] = [];
    let i = ''
    for(let parenthesis of s){
        if (stack.length > 0 && stack[stack.length-1]+parenthesis === "()"){
            i += (stack.pop() + parenthesis);
        } else {
            stack.push(parenthesis)
        }
    };
    return i.length
};

console.log(findLongestParentheses())