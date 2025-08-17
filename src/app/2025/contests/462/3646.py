'''
3646. Next Special Palindrome Number

    You are given an integer n.

    A number is called special if:

    It is a palindrome.
    Every digit k in the number appears exactly k times.
    Return the smallest special number strictly greater than n.

    Example 1:

    Input: n = 2

    Output: 22

    Explanation:

    22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.

    Example 2:

    Input: n = 33

    Output: 212

    Explanation:

    212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.
'''
from typing import List
from functools import cache

MS=18; dp:List[List[int]] = [[] for _ in range(MS)]

@cache
def dfs(x):
    dp[x].append(x)
    tp = [x]; x = x+1 if x&1 else x+2
    while (x<=8):
        for csm in dfs(x):
            if x+csm >= MS: break
            tp.append(x+csm)
            dp[x+csm].append(x|csm)
        x+=2
    return tp

for x in range(1,9): dfs(x)

for i,x in enumerate(dp):
    print(f'i={i}, x={[ bin(c) for c in x]}')


class Solution:
    def specialPalindrome(self, n: int) -> int:
        # Observation: Using 2 odd digits is never possible to get right answer!
        pass