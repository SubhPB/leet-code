class Solution:
    '''
    3983. Subsequence After One Replacement
    You are given two strings s and t consisting of lowercase English letters.
    You may choose at most one index in s and replace the character at that index with any lowercase English letter.
    Return true if it is possible to make s a subsequence of t; otherwise, return false.

    Example 1:
    Input: s = "cat", t = "chat"
    Output: true
    Explanation:
    Replace s[1] from 'a' to 'h'. The resulting string is "cht".
    "cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.

    Constraints:
    1 <= s.length, t.length <= 10**5
    s and t consist only of lowercase English letters.
    '''
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        dt={}
        for i,ct in enumerate(t):
            if ct not in dt:dt[ct]=[]
            dt[ct].append(i)
        prev=-1; n=len(t); used=0
        for ch in s:
            z=len(dt[ch] if ch in dt else [])
            l=0; r=z
            while l<r:
                m=(l+r)//2
                idx=dt[ch][m]
                if idx>prev:
                    r=m
                else:
                    l=m+1
            if l>=z:
                used+=1
                prev+=1
                if used>1 or prev>=n:
                    return False
            else: prev=dt[ch][l]
        return True 