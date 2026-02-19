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