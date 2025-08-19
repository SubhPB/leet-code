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

    python src/app/2025/contests/462/3646.py
'''
from typing import List
from collections import deque

dp:List[List[int]] = [
    [] for _ in range(sum([2,4,6,8,10]))
]

def dfs(px:int):
    mask:List[int] = []; tn:List[int] = []
    for x in [2,4,6,8]:
        tn.append(px); mask.append((1<<px) if px else 0)
        for i, sm in enumerate(tn):
            totalSm = x+sm; newMask = mask[i] | 1<<x
            dp[totalSm].append(newMask)
            tn[i]=totalSm; mask[i]=newMask

dfs(0) # calculating dp for even only nums

for px in [3,5,7,9]:  # calculating dp evens + one odd scenario
    dfs(px)
    dp[px].append(1<<px) # obvious base-cases for odd nums


class Solution:
    def specialPalindrome(self, n: int) -> int:
        d = len(str(n)); res = float('inf')
        # Observation: Using 2 odd digits is never possible to get right answer!
        #    To get the minimum result we will try to find smallest candidate of same digit length as of n
        #    If not found then we'll find smallest digit num with the digit length eql 'd+1', which is definitely an answer!

        def hlfParse(x:List[int|str], m=[]):
            return int(''.join(x + m + x.reverse()))
        
        
        if not d%2:
            # let's look for a candidate greater and having digit length as of 'd'
            for candidate in dp[d]:
                digits:List[int] = []
                for i in range(candidate.bit_length()-1, -1, -1):
                    if candidate&(1<<i): digits.append(i)
                
                hlf = []
                for x in digits:
                    for i in range(x//2): hlf.append(x)

                maxPossible = hlfParse(hlf)
                if n<maxPossible:
                    res = min(res, maxPossible)
                    left, right = hlf[:1], deque(hlf[1:])
                    while right:
                        for digit in digits:
                                pass

        else:
            pass

        return res
