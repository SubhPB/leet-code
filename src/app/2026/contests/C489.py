from collections import Counter
from typing import List
class Solution:
    '''
    3843. First Element with Unique Frequency
    You are given an integer array nums.
    Return an integer denoting the first element (scanning from left to right) in nums whose frequency is unique. That is, no other integer appears the same number of times in nums. If there is no such element, return -1.

    Example 1:
    Input: nums = [20,10,30,30]
    Output: 30
    Explanation:

    20 appears once.
    10 appears once.
    30 appears twice.
    The frequency of 30 is unique because no other integer appears exactly twice.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    '''
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt=Counter(nums); dt={}
        for e in set(nums):
            dt[cnt[e]]=1+dt.get(cnt[e],0)
        for e in nums: 
            if dt[cnt[e]]==1: return e
        return -1
    '''
    3844. Longest Almost-Palindromic Substring

    You are given a string s consisting of lowercase English letters.
    A substring is almost-palindromic if it becomes a palindrome after removing exactly one character from it.
    Return an integer denoting the length of the longest almost-palindromic substring in s.

    Example 1:
    Input: s = "abca"
    Output: 4
    Explanation:
    Choose the substring "abca".
    Remove "abca".
    The string becomes "aba", which is a palindrome.
    Therefore, "abca" is almost-palindromic.

    Constraints:
    2 <= s.length <= 2500
    s consists of only lowercase English letters.
    '''
class Solution:
    def almostPalindromic(self, s: str) -> int:
        n=len(s); dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(n-1,-1,-1):
                if s[i-1]==s[j]:
                    dp[i][j]=1+dp[i-1][j+1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j+1])
        for i in range(1,n+1):
            for j in range(n-1,-1,-1):
                if s[i-1]==s[j]:
                    dp[i][j]=1+dp[i-1][j+1]
              
        return min(n,1+dp[n][0])
    '''
    3845. Maximum Subarray XOR with Bounded Range

    You are given a non-negative integer array nums and an integer k.
    You must select a subarray of nums such that the difference between its maximum and minimum elements is at most k. The value of this subarray is the bitwise XOR of all elements in the subarray.
    Return an integer denoting the maximum possible value of the selected subarray.

    Example 1:
    Input: nums = [5,4,5,6], k = 2
    Output: 7
    Explanation:
    Select the subarray [5, 4, 5, 6].
    The difference between its maximum and minimum elements is 6 - 4 = 2 <= k.
    The value is 4 XOR 5 XOR 6 = 7.
    Constraints:
    1 <= nums.length <= 4 * 10^4
    0 <= nums[i] < 2^15
    0 <= k < 2^15
    '''
    def maxXor(self, nums: list[int], k: int) -> int:
        pass