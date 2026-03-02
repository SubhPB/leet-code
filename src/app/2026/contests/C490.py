class Solution:
    '''
    3848. Check Digitorial Permutation

    You are given an integer n.
    A number is called digitorial if the sum of the factorials of its digits is equal to the number itself.
    Determine whether any permutation of n (including the original order) forms a digitorial number.
    Return true if such a permutation exists, otherwise return false.
    Note:
    The factorial of a non-negative integer x, denoted as x!, is the product of all positive integers less than or equal to x, and 0! = 1.
    A permutation is a rearrangement of all the digits of a number that does not start with zero. Any arrangement starting with zero is invalid.
    
    Example 1:
    Input: n = 145
    Output: true
    Explanation:
    The number 145 itself is digitorial since 1! + 4! + 5! = 1 + 24 + 120 = 145. Thus, the answer is true.

    Constraints:
    1 <= n <= 10^9
    '''
    def isDigitorialPermutation(self, n: int) -> bool:
        fx=[1]*10; fd={}
        for i in range(1,10): fx[i]=i*fx[i-1]
        x=sum([fx[int(d)] for d in str(n)])
        for d in str(x): fd[d]=1+fd.get(d,0)
        if len(str(x))!=len(str(n)): return False
        for d in str(n):
            if not fd.get(d,0): return False
            fd[d]-=1;  
        return True
    '''
    3849. Maximum Bitwise XOR After Rearrangement

    You are given two binary strings s and t​​​​​​​, each of length n.
    You may rearrange the characters of t in any order, but s must remain unchanged.
    Return a binary string of length n representing the maximum integer value obtainable by taking the bitwise XOR of s and rearranged t.

    Example 1:
    Input: s = "101", t = "011"
    Output: "110"
    Explanation:

    One optimal rearrangement of t is "011".
    The bitwise XOR of s and rearranged t is "101" XOR "011" = "110", which is the maximum possible.

    Constraints:
    1 <= n == s.length == t.length <= 2 * 10^5
    s[i] and t[i] are either '0' or '1'.
    '''
    def maximumXor(self, s: str, t: str) -> str:
        r=0; n=len(s)
        x=t.count("1"); y=n-x
        for i,d in enumerate(s):
            if int(d) and y:
                r+=(1<<(n-i-1)); y-=1
            elif (not int(d)) and x:
                r+=(1<<(n-i-1)); x-=1
        if not r: return "0"*n
        return "0"*(n-r.bit_length())+bin(r)[2:]