from typing import List
class Solution:
    '''
    3810. Minimum Operations to Reach Target Array

    You are given two integer arrays nums and target, each of length n, 
    where nums[i] is the current value at index i and target[i] is the desired value at index i.
    You may perform the following operation any number of times (including zero):
    Choose an integer value x
    Find all maximal contiguous segments 
    where nums[i] == x (a segment is maximal if it cannot be extended to the left or right while keeping all values equal to x)
    For each such segment [l, r], update simultaneously:
    nums[l] = target[l], nums[l + 1] = target[l + 1], ..., nums[r] = target[r]
    Return the minimum number of operations required to make nums equal to target.

    Example 1:
    Input: nums = [1,2,3], target = [2,1,3]
    Output: 2

    Explanation:​​​​​​​
    Choose x = 1: maximal segment [0, 0] updated -> nums becomes [2, 2, 3]
    Choose x = 2: maximal segment [0, 1] updated (nums[0] stays 2, nums[1] becomes 1) -> nums becomes [2, 1, 3]
    Thus, 2 operations are required to convert nums to target.​​​​​​​​​​​​​​

    Constraints:
    1 <= n == nums.length == target.length <= 10^5
    1 <= nums[i], target[i] <= 10^5
    '''
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        freq={}; n=len(nums)
        for i in range(n):
            if nums[i]!=target[i]: freq[nums[i]]=1+freq.get(nums[i],0)
        return len(freq)