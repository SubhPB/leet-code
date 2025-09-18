'''
3685. Subsequence Sum After Capping Elements

    You are given an integer array nums of size n and a positive integer k.

    An array capped by value x is obtained by replacing every element nums[i] with min(nums[i], x).

    For each integer x from 1 to n, determine whether it is possible to choose a subsequence from the array capped by x such that the sum of the chosen elements is exactly k.

    Return a 0-indexed boolean array answer of size n, where answer[i] is true if it is possible when using x = i + 1, and false otherwise.


    Example 1:

    Input: nums = [4,3,2,4], k = 5

    Output: [false,false,true,true]

    Explanation:

    For x = 1, the capped array is [1, 1, 1, 1]. Possible sums are 1, 2, 3, 4, so it is impossible to form a sum of 5.
    For x = 2, the capped array is [2, 2, 2, 2]. Possible sums are 2, 4, 6, 8, so it is impossible to form a sum of 5.
    For x = 3, the capped array is [3, 3, 2, 3]. A subsequence [2, 3] sums to 5, so it is possible.
    For x = 4, the capped array is [4, 3, 2, 4]. A subsequence [3, 2] sums to 5, so it is possible.
    Example 2:

    Input: nums = [1,2,3,4,5], k = 3

    Output: [true,true,true,true,true]

    Explanation:

    For every value of x, it is always possible to select a subsequence from the capped array that sums exactly to 3.

    Constraints:

        1 <= n == nums.length <= 4000
        1 <= nums[i] <= n
        1 <= k <= 4000
'''
from typing import List
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort(); n = len(nums); res = [False]*n
        for x in range(1,n+1):
            dp = [not i for i in range(k+1)]
            for num in nums:
                num = min(num,x)
                for j in range(k,-1,-1):
                    if j-num<0: break 
                    elif dp[j-num]: dp[j]=True
            res[x-1]=dp[k]
        return res
 
    def subsequenceSumAfterCapping2(self, nums: List[int], k: int) -> List[bool]:
        nums.sort(); n = len(nums)
        res = [False]*n
        for x in range(1,n+1):
            i=0
            dp = [not i for i in range(k+1)]
            while i<n and nums[i]<x:
                for j in range(k,nums[i]-1,-1):
                    if dp[j-nums[i]]: dp[j]=True
                i+=1
            nes = n-i; ne = 0
            while not res[x-1] and ne<=nes and k>=ne*x:
                if dp[k-ne*x]: res[x-1]=True
                ne+=1
            
        return res