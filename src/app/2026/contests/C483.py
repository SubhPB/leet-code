from typing import List
class Solution:
    '''
    3799. Word Squares II
    You are given a string array words, consisting of distinct 4-letter strings, each containing lowercase English letters.
    A word square consists of 4 distinct words: top, left, right and bottom, arranged as follows:

    top forms the top row.
    bottom forms the bottom row.
    left forms the left column (top to bottom).
    right forms the right column (top to bottom).
    It must satisfy:

    top[0] == left[0], top[3] == right[0]
    bottom[0] == left[3], bottom[3] == right[3]
    Return all valid distinct word squares, sorted in ascending lexicographic order by the 4-tuple (top, left, right, bottom)​​​​​​​.

    Constraints:
    4 <= words.length <= 15
    words[i].length == 4
    words[i] consists of only lowercase English letters.
    All words[i] are distinct.
    '''
    def wordSquares(self, w: List[str]) -> List[List[str]]:
        res=[]; n=len(w)
        for t in range(n):
            for l in range(n):
                if w[t][0]!=w[l][0]: continue
                for b in range(n):
                    if w[b][0]!=w[l][3]: continue
                    for r in range(n):
                        if len(set((t,l,b,r)))!=4 or w[b][3]!=w[r][3] or w[t][3]!=w[r][0]: continue
                        res.append([w[x] for x in [t,l,r,b]])
        return sorted(res)
    '''
    3800. Minimum Cost to Make Two Binary Strings Equal
    You are given two binary strings s and t, both of length n, and three positive integers flipCost, swapCost, and crossCost.
    You are allowed to apply the following operations any number of times (in any order) to the strings s and t:
    Choose any index i and flip s[i] or t[i] (change '0' to '1' or '1' to '0'). The cost of this operation is flipCost.
    Choose two distinct indices i and j, and swap either s[i] and s[j] or t[i] and t[j]. The cost of this operation is swapCost.
    Choose an index i and swap s[i] with t[i]. The cost of this operation is crossCost.
    Return an integer denoting the minimum total cost needed to make the strings s and t equal.

    Example 1:
    Input: s = "01000", t = "10111", flipCost = 10, swapCost = 2, crossCost = 2
    Output: 16
    Explanation:
    We can perform the following operations:
    Swap s[0] and s[1] (swapCost = 2). After this operation, s = "10000" and t = "10111".
    Cross swap s[2] and t[2] (crossCost = 2). After this operation, s = "10100" and t = "10011".
    Swap s[2] and s[3] (swapCost = 2). After this operation, s = "10010" and t = "10011".
    Flip s[4] (flipCost = 10). After this operation, s = t = "10011".
    The total cost is 2 + 2 + 2 + 10 = 16.

    Constraints:
    n == s.length == t.length
    1 <= n <= 10^5​​​​​​​
    1 <= flipCost, swapCost, crossCost <= 10^9
    s and t consist only of the characters '0' and '1'.
  
    '''
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        n=len(s); m=0; x=0
        for i in range(n): 
            if s[i]!=t[i]: 
                m+=1; x+=int(s[i])
        if 2*flipCost<=min(swapCost,crossCost): return m*flipCost
        cost=0; inf=10**9+7
        while x>0 and m!=max(x,m-x):
           sc = swapCost if m-x-1>0 else inf
           cc = crossCost if x-1>0 else inf
           cost+=min(sc,cc)
           if sc<cc: x-=1
           else: x-=2
           m-=2
        return cost+min(
            m*flipCost, 
            ((m+1)//2)*crossCost + (m%2)*flipCost
        )