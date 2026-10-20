class Solution:
    '''
    4031. Find All Numbers Disappeared in an Array II

    You are given an integer array nums and two integers lower and upper.
    A missing integer is an integer in the inclusive range [lower, upper] that does not appear in nums.
    Return a 2D integer array where each element is of the form [start, end], representing a contiguous range of missing integers. Return the ranges in increasing order. If there are no missing integers, return an empty array.
    Note: Consecutive missing integers should be grouped into a single range.
    
    Example 1:

    Input: nums = [3,9,7], lower = 1, upper = 12
    Output: [[1,2],[4,6],[8,8],[10,12]]


    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**5
    1 <= lower <= upper <= 10**5
    '''
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        pass