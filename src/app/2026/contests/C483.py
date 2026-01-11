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