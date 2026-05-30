class Solution:
    '''
    3922. Minimum Flips to Make Binary String Coherent

    You are given a binary string s.
    A string is considered coherent if it does not contain "011" or "110" as subsequences.
    In one operation, you can flip any character in s ('0' to '1' or '1' to '0').
    Return an integer denoting the minimum number of operations required to make s coherent.
    Example 1:
    Input: s = "1010"
    Output: 1
    Explanation:
    Flip s[0] to get "0010", which contains no "011" or "110" subsequences.

    Constraints:
    1 <= s.length <= 10**5
    s[i] is either '0' or '1'.
    '''
    def minFlips(self, s: str) -> int:
        n=len(s); x=s.count('1')
        f,b=0,0; fg=False
        for i,k in enumerate(s):
            if int(k):
                f+=1; 
            elif f>1: fg=True
    
            if int(s[n-i-1]):
                b+=1
            elif b>1: fg=True
               
        if fg:
            return min(
                abs(x-1),n-x,x
            )
        return 0