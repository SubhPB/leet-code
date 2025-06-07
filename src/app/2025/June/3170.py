'''
3170. Lexicographically Minimum String After Removing Stars

    You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

    While there is a '*', do the following operation:

    Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
    Return the lexicographically smallest resulting string after removing all '*' characters.

    Example 1:

    Input: s = "aaba*"

    Output: "aab"

    Explanation:

    We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

    Example 2:

    Input: s = "abc"

    Output: "abc"

    Explanation:

    There is no '*' in the string.

    Constraints:

    1 <= s.length <= 105
    s consists only of lowercase English letters and '*'.
    The input is generated such that it is possible to delete all '*' characters.
'''

import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        
        idx = lambda x:ord(x)-97
        res, n = [], len(s)
        rec = [[] for i in range(26)]

        mnchars = []
        i=0
        while i<n:
            c = s[i]
            if c != '*':
                rec[idx(c)].append(len(res))
                res.append(c)
                if len(rec[idx(c)])==1: heapq.heappush(mnchars, c)
            elif len(mnchars):
                mnchar = mnchars[0]
                at = rec[idx(mnchar)].pop()
                res[at] = ''
                if not rec[idx(mnchar)]: heapq.heappop(mnchars)
            i+=1
        return ''.join(res)