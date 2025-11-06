from typing import List
class Solution:
    '''
    3719. Longest Balanced Subarray I

    You are given an integer array nums.
    A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
    Return the length of the longest balanced subarray.

    Example 1:
    Input: nums = [2,5,4,3]
    Output: 4

    Explanation:
    The longest balanced subarray is [2, 5, 4, 3].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

    Constraints:

    1 <= nums.length <= 1500
    1 <= nums[i] <= 10^5
    '''
    def longestBalanced(self, nums: List[int]) -> int:
        e,o=0,0;freq={(0,0):-1};res=0
        for i,num in enumerate(nums):
            if not num in freq:
                if num%2: o+=1 
                else: e+=1
                freq[num]=1
            if not (e,o) in freq: freq[(e,o)]=i
            x=min(e,o)
            if x and (e-x,o-x) in freq: res=max(res,i-freq[(e-x,o-x)])
        return res