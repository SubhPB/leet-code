'''
2014. Longest Subsequence Repeated k Times
    You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

    A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

    A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

    For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
    Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

    

    Example 1:

    example 1
    Input: s = "letsleetcode", k = 2
    Output: "let"
    Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
    "let" is the lexicographically largest one.
    Example 2:

    Input: s = "bb", k = 2
    Output: "b"
    Explanation: The longest subsequence repeated 2 times is "b".
    Example 3:

    Input: s = "ab", k = 2
    Output: ""
    Explanation: There is no subsequence repeated 2 times. Empty string is returned.
    

    Constraints:

    n == s.length
    2 <= n, k <= 2000
    2 <= n < k * 8
    s consists of lowercase English letters.

    python ./src/app/2025/June/2014.py
'''

from itertools import  permutations
from collections import Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        for char in [*freq.keys()]:
            if freq[char] < k: del freq[char]
        if not len(freq): return ""

        ns = []
        for char in s:
            if char in freq: ns.append(char)
        ns = ''.join(ns)

        # if m = subSeq.length then 1 <= m <= len(ns)//k
        # "char" at most can be used freq['char']//k
        subSeq, subSeqChars = '', []
        for char in freq: 
            subSeqChars += [char]*(freq[char]//k)
            if char > subSeq: subSeq = char

        def isSubSeqK(ps:str, seq:str):
            i, j, r, m = 0, 0, 0, len(seq)
            while i<len(ps) and r<k:
                if ps[i] == seq[j]:
                    j += 1
                    r += j//m
                    j %= m
                i+=1
            return r==k
        
        l, r = 1, len(ns)//k

        while l<r:
            tempSeq, m = '', (l+r+1)//2 #Using ceil because 'l' always hold a true value
            computed:dict[str,bool] = {}
            # if m==7: print(f'l={l} r={r} m={m} seq={subSeq} combs={list(permutations(subSeqChars,m))}')
            for seqComb in permutations(subSeqChars, m):
                seq = ''.join(seqComb)
                if not seq in computed and seq > tempSeq and isSubSeqK(ns, seq):
                    tempSeq = seq
                    computed[seq]=True
            if tempSeq:
                subSeq = tempSeq
                l = m
            else: #no change found!
                r = m-1

        return subSeq
    

if __name__ == '__main__':
    testcases:list[list[str, int]] = []
    addcase = lambda s,k: testcases.append([s,k])

    addcase(s = "letsleetcode", k = 2)
    addcase(s = "bb", k = 2)
    addcase(s = "ab", k = 2)
    addcase(s="mciuctbmciuctb", k=2)
    sol = Solution()
    for [s,k] in testcases:
        print(f's="{s}" k="{k}" subseq="{sol.longestSubsequenceRepeatedK(s,k)}"')