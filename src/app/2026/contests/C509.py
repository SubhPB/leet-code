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
        pass