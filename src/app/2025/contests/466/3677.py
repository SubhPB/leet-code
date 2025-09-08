'''
    3677. Count Binary Palindromic Numbers

    You are given a non-negative integer n.

    A non-negative integer is called binary-palindromic if its binary representation (written without leading zeros) reads the same forward and backward.

    Return the number of integers k such that 0 <= k <= n and the binary representation of k is a palindrome.

    Note: The number 0 is considered binary-palindromic, and its representation is "0".

    

    Example 1:

    Input: n = 9

    Output: 6

    Explanation:

    The integers k in the range [0, 9] whose binary representations are palindromes are:

    0 → "0"
    1 → "1"
    3 → "11"
    5 → "101"
    7 → "111"
    9 → "1001"
    All other values in [0, 9] have non-palindromic binary forms. Therefore, the count is 6.

    Example 2:

    Input: n = 0

    Output: 1

    Explanation:

    Since "0" is a palindrome, the count is 1.

    

    Constraints:

    0 <= n <= 10^15
'''
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        res=1
        if n>=1: res+=1

        def strRev(x:str):
            ls = list(x); n = len(x)
            for i in range(n):
                ls[i] = x[n-i-1]
            return ''.join(ls)
        def parse(x:str):
            return int(f'0b{x}',2)
        
        def dfs(x:str,w:int):
            hf = w//2
            if len(x) == hf:
                if w&1:
                    cnt = 0
                    for m in "01":
                        if parse(x+m+strRev(x)) <=n: cnt+=1
                    return cnt
                else:
                    if parse(x+strRev(x)) <= n: return 1
                    else: return 0
            else:
                cnt=0
                for bn in "01":
                    cnt+= dfs(x+bn,w)
                return cnt
            
        for p in range(1,51):
            pow = 2**p
            if pow > n: break
            w = p+1; res += dfs("1",w)

        return res