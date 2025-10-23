
from typing import List
from collections import Counter
from bisect import bisect_right as br, bisect_left as bl
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int: 
        '''
            3347. Maximum Frequency of an Element After Performing Operations II

            You are given an integer array nums and two integers k and numOperations.
            You must perform an operation numOperations times on nums, where in each operation you:
            Select an index i that was not selected in any previous operations.
            Add an integer in the range [-k, k] to nums[i].
            Return the maximum possible frequency of any element in nums after performing the operations.    

            Example 1:
            Input: nums = [1,4,5], k = 1, numOperations = 2
            Output: 2
            Explanation:
            We can achieve a maximum frequency of two by:

            Adding 0 to nums[1], after which nums becomes [1, 4, 5].
            Adding -1 to nums[2], after which nums becomes [1, 4, 4].

            Adding 0 to nums[1].
            
            Constraints:
            1 <= nums.length <= 10^5
            1 <= nums[i] <= 10^9
            0 <= k <= 10^9
            0 <= numOperations <= nums.length
        '''
        counter=Counter(nums)
        nums=sorted(list(counter.keys()))
        n=len(nums);lower=[];upper=[]; res=1
        for num in nums: # will come back to this!
            lower.append(num-k); upper.append(num+k)
        for i,num in enumerate(nums):
            l=bl(upper,num-k); r=br(lower,num+k)
            t=r-l+1
        return res
    '''
    3461. Check If Digits Are Equal in String After Operations I

    You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
    For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
    Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
    Return true if the final two digits in s are the same; otherwise, return false.

    Example 1:

    Input: s = "3902"

    Output: true

    Explanation:

    Initially, s = "3902"
    First operation:
    (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
    (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
    (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
    s becomes "292"
    Second operation:
    (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
    (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
    s becomes "11"
    Since the digits in "11" are the same, the output is true.

    Constraints:

    3 <= s.length <= 100
    s consists of only digits.
    '''
    def hasSameDigits(self, s: str) -> bool:
        x=[int(z) for z in s]
        while len(x)>2:
            nx=[]
            for i in range(1,len(x)): nx.append((x[i-1]+x[i])%10)
            x=nx
        return x[0]==x[1]