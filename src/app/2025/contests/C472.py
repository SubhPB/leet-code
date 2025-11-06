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
        n=len(nums);res=0
        for i in range(n):
            cnt=[0,0];freq={}
            for j in range(i,n):
                num=nums[j]
                if num not in freq:
                    freq[num]=1
                    cnt[num%2]+=1
                if cnt[0]==cnt[1]: res=max(res,j-i+1)
        return res