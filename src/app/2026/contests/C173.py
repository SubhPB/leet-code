from typing import List
class Solution:
    '''
    3795. Minimum Subarray Length With Distinct Sum At Least K
    You are given an integer array nums and an integer k.
    Return the minimum length of a subarray whose sum of the distinct values present in that subarray (each value counted once) is at least k. If no such subarray exists, return -1.
    
    Example 1:
    Input: nums = [2,2,3,1], k = 4
    Output: 2
    Explanation:
    The subarray [2, 3] has distinct elements {2, 3} whose sum is 2 + 3 = 5, which is ​​​​​​​at least k = 4. Thus, the answer is 2.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= k <= 10^9
    '''
    def minLength(self, nums: List[int], k: int) -> int:
        return -1