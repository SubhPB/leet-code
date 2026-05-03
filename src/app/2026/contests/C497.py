'''
3900. Longest Balanced Substring After One Swap

You are given a binary string s consisting only of characters '0' and '1'.
A string is balanced if it contains an equal number of '0's and '1's.
You can perform at most one swap between any two characters in s. Then, you select a balanced substring from s.
Return an integer representing the maximum length of the balanced substring you can select.

Example 1:
Input: s = "100001"
Output: 4
Explanation:
Swap "100001". The string becomes "101000".
Select the substring "101000", which is balanced because it has two '0's and two '1's.

Constraints:
1 <= s.length <= 10**5
s consists only of the characters '0' and '1'.
'''
class Solution:
    def longestBalanced(self, s: str) -> int:
        dt={}; res=0; x=0
        for i,b in enumerate(s):
            x+=int(b); df=2*x-i-1 #x-o
            res=max(
                res,
                i-min(
                    dt.get(df-2,i),
                    dt.get(df+2,i),
                    dt.get(df,i)
                )
            )
            if not df: res=max(res,i+1)
            if df not in dt: dt[df]=i
        return res