'''
3660. Jump Game IX
    You are given an integer array nums.

    From any index i, you can jump to another index j under the following rules:

    Jump to index j where j > i is allowed only if nums[j] < nums[i].
    Jump to index j where j < i is allowed only if nums[j] > nums[i].
    For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

    Return an array ans where ans[i] is the maximum value reachable starting from index i.

    

    Example 1:

    Input: nums = [2,1,3]

    Output: [2,2,3]

    Explanation:

    For i = 0: No jump increases the value.
    For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
    For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
    Thus, ans = [2, 2, 3].

    Example 2:

    Input: nums = [2,3,1]

    Output: [3,3,3]

    Explanation:

    For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
    For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
    For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
    Thus, ans = [3, 3, 3].

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
'''
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n=len(nums);res = [*nums]
        left = [0]*n; right = [n-1]*n

        for i in range(1,n):
            left[i]=left[i-1]
            if nums[i]>nums[left[i-1]]: left[i]=i
            r = n-i-1
            right[r]=right[r+1]
            if nums[r]<nums[right[r+1]]: right[r]=r
        
        rt=n-1
        while rt>0:
            x = left[rt]; y = right[x]
            maxVal = nums[x]; minVal = nums[y]
            l=0; r=rt
            while l<r:
                m=(l+r)//2; z = left[m]
                minVal = min(minVal, nums[right[r]])
                if nums[z]>minVal: r=m; l=0
                else: l=m+1
            for i in range(l,rt+1): res[i]=maxVal
            rt=l-1

        return res