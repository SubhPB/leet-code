
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
        n=len(s); m=len(t)
        i=0; j=0

        dt={}
        for ch in t: dt[ch]=1+dt.get(ch,0)

        used=0
        curr={}
        while i<n and j<m:
            ch=s[i]; ct=t[i]
            if ch not in curr:
                curr[ch]=0

            if ch==ct:
                curr[ch]+=1
                i+=1
            else:
                # prévoir, si 'ch' existe dans 't' reste
                cnt=dt.get(ch,0)-curr[ch]
                if cnt<=0:
                    used+=1
                    i+=1

            if used>1: return False #un change nécessaire
            j+=1

        if i==n: return True

        # même intuition mais à l'envers
        used=0
        curr={}
        i=n-1; j=m-1
        while j>=0 and i>=0:
            ch=s[i]; ct=t[j]
            if ch not in curr: 
                curr[ch]=0
            if ch==ct:
                curr[ch]+=1
                i-=1
            else:
                cnt=dt.get(ch,0)-curr[ch]
                if cnt<=0:
                    used+=1
                    i-=1
            if used>1: return False
            j-=1
        return i==-1