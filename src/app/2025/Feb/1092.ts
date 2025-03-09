/**
 * 1092. Shortest Common Supersequence 

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 */
class Solve1092{
    constructor(public s1:string,public s2:string){
        this.s1=s1; this.s2=s2;
    };
    solution1(s1=this.s1,s2=this.s2){
        /**
         * Best case: If any of string is already a substring of other string.
         * Worst case: There were no common chars in b/w them 
         */
        const [str1,str2] = [s1,s2].sort((a,b)=>b.length-a.length); //Descending order
        if (str1.indexOf(str2)!==-1) return str1;
        /**
         * Two ways to join strings, either from front or back
         */
        let i=0;
        while(i<str2.length&&str2[i]===str1[str1.length-i-1]) i++;
    }
}