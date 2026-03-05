/**
 * 3853. Merge Close Characters
You are given a string s consisting of lowercase English letters and an integer k.
Two equal characters in the current string s are considered close if the distance between their indices is at most k.
When two characters are close, the right one merges into the left. Merges happen one at a time, and after each merge, the string updates until no more merges are possible.
Return the resulting string after performing all possible merges.
Note: If multiple merges are possible, always merge the pair with the smallest left index. If multiple pairs share the smallest left index, choose the pair with the smallest right index.
 
Example 1:
Input: s = "abca", k = 3
Output: "abc"
Explanation:
​​​​​​​Characters 'a' at indices i = 0 and i = 3 are close as 3 - 0 = 3 <= k.
Merge them into the left 'a' and s = "abc".
No other equal characters are close, so no further merges occur.

Constraints:
1 <= s.length <= 100
1 <= k <= s.length
s consists of lowercase English letters.
 */

class BiweeklyContest177 {
    mergeCharacters(s: string, k: number): string {
        const res:string[]=[s[0]], prev={[s[0]]:0};
        const n=s.length, g=Array.from({length:n},()=>0);
        for(let i=1; i<n; i++){
            g[i]=g[i-1]
            if (s[i] in prev){
                const t=i-prev[s[i]]+1-(g[prev[s[i]]]-g[i]);
                if (t<=k){
                    g[i]+=1; delete prev[s[i]]
                } else {
                    prev[s[i]]=i;
                }
            };
            if (!(s[i] in prev)){
                res.push(s[i]);
                prev[s[i]]=i;
            };
        };
        return res.join('');
    };
}