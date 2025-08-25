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
        n = len(nums); left = [0]*n; right = [n-1]*n

        for i in range(n):
            left[i] = i if nums[i]>nums[left[max(0,i-1)]] else left[max(0,i-1)]
            j = n-i-1
            right[j] = j if nums[j]<nums[right[min(j+1,n-1)]] else right[min(j+1,n-1)]
        
        x = left[-1]; r = n; mn = nums[right[x]]
        while x>=0:
            for i in range(x+1,r): nums[i]=nums[x]
            if x:
                r=x; x-=1
                if nums[left[x]]>mn:
                    lt=0; rt=x
                    while lt<rt:
                        m = (lt+rt)//2
                        if nums[left[m]]>mn: rt=m
                        else: lt=m+1
                    x=lt; mn=min(mn,nums[right[x]])
                else:
                    x = left[x]

        return nums