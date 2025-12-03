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

        