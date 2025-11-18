class Solution:
    '''
        3746. Minimum String Length After Balanced Removals
        You are given a string s consisting only of the characters 'a' and 'b'.
        You are allowed to repeatedly remove any substring where the number of 'a' characters is equal to the number of 'b' characters.
        After each removal, the remaining parts of the string are concatenated together without gaps.
        Return an integer denoting the minimum possible length of the string after performing any number of such operations.

        Example 1:
        Input: s = "aabbab"
        Output: 0

        Explanation:
        The substring "aabbab" has three 'a' and three 'b'. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

        Example 2:
        Input: s = "aaaa"

        Output: 4
        Explanation:
        Every substring of "aaaa" contains only 'a' characters. No substring can be removed as a result, so the minimum length remains 4.

        Constraints:

        1 <= s.length <= 10^5
        s[i] is either 'a' or 'b'
    '''
    def minLengthAfterRemovals(self, s: str) -> int:
        a=s.count('a');b=len(s)-a
        return abs(a-b)
    '''
    3747. Count Distinct Integers After Removing Zeros
    You are given a positive integer n.
    For every integer x from 1 to n, we write down the integer obtained by removing all zeros from the decimal representation of x.
    Return an integer denoting the number of distinct integers written down.

    Example 1:
    Input: n = 10
    Output: 9
    Explanation:
    The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).

    Constraints:
    1 <= n <= 10^15
    '''
    def countDistinct(self, n: int) -> int:
        digits=[int(dgt) for dgt in str(n)]
        l=len(digits); fn=lambda N:-1+((9**(N)-1)//(9-1))
        i=0;res=fn(l)+1 # inc by 1 because n is itself unique if not include zero (assumed it not has zero)
        while i<l:
            if not digits[i]: 
                res-=1; break # it had zero, pre-assumption was false! 
            res+=(digits[i]-1)*(9**(l-i-1))
            i+=1
        return res