'''
3788. Maximum Score of a Split

You are given an integer array nums of length n.
Choose an index i such that 0 <= i < n - 1.
For a chosen split index i:
Let prefixSum(i) be the sum of nums[0] + nums[1] + ... + nums[i].
Let suffixMin(i) be the minimum value among nums[i + 1], nums[i + 2], ..., nums[n - 1].
The score of a split at index i is defined as:
score(i) = prefixSum(i) - suffixMin(i)
Return an integer denoting the maximum score over all valid split indices.

Example 1:
Input: nums = [10,-1,3,-4,-5]
Output: 17
Explanation:
The optimal split is at i = 2, score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17.

Constraints:
2 <= nums.length <= 10^5
-109​​​​​​​ <= nums[i] <= 10^9
'''
from typing import List
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        res=None; n=len(nums); t=0; mins=[nums[-1]]*n
        for i in range(n-2,-1,-1): mins[i]=min(nums[i],mins[i+1])
        for i in range(n-1):
            t+=nums[i]
            res=t-mins[i+1] if res is None else max(res,t-mins[i+1])
        return res