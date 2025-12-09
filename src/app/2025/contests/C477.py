from typing import List
class Solution:
    '''
    3755. Find Maximum Balanced XOR Subarray Length

    Given an integer array nums, return the length of the longest subarray,
    that has a bitwise XOR of zero and contains an equal number of even and odd numbers. 
    If no such subarray exists, return 0.

    Example 1:
    Input: nums = [3,1,3,2,0]
    Output: 4
    Explanation:
    The subarray [1, 3, 2, 0] has bitwise XOR 1 XOR 3 XOR 2 XOR 0 = 0 and contains 2 even and 2 odd numbers.

    Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    '''
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        xor=0;df=0;res=0;hash={(0,0):-1}
        for i,num in enumerate(nums):
            xor^=num;df+=[1,0][num%2]-[0,1][num%2]
            if (xor,df) in hash: res=max(res,i-hash[(xor,df)])
            else: hash[(xor,df)]=i
        return res
    '''
    3757. Number of Effective Subsequences
    You are given an integer array nums.
    The strength of the array is defined as the bitwise OR of all its elements.
    A subsequence is considered effective if removing that subsequence strictly decreases the strength of the remaining elements.
    Return the number of effective subsequences in nums. Since the answer may be large, return it modulo 109 + 7.
    The bitwise OR of an empty array is 0.

    Example 1:
    Input: nums = [1,2,3]
    Output: 3
    Explanation:
    The Bitwise OR of the array is 1 OR 2 OR 3 = 3.
    Subsequences that are effective are:
    [1, 3]: The remaining element [2] has a Bitwise OR of 2.
    [2, 3]: The remaining element [1] has a Bitwise OR of 1.
    [1, 2, 3]: The remaining elements [] have a Bitwise OR of 0.
    Thus, the total number of effective subsequences is 3.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    '''
    def countEffective(self, nums: List[int]) -> int:
        '''
            Intuition basis W #subsequences = 2^n - 1 
            <--G1-->,num,<--G2-->,num,...,num,<--Gn-->
        '''
        pass