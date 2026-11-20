class Solution:
    '''
    4044. Count Good Cyclic Rotations

    You are given an integer array nums of even length n.
    A cyclic rotation of nums is obtained by choosing a prefix of nums whose length is between 0 and n - 1 (inclusive), and moving it to the end of the array while preserving the order of all elements.
    A cyclic rotation is good if the sum of its first n / 2 elements is strictly greater than the sum of its last n / 2 elements.
    Return the number of cyclic rotations of nums that are good.

    Example 1:
    Input: nums = [1,2,3,4,5,6]

    Output: 3

    Constraints:
    2 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    n is even.
    '''
    def countGoodRotations(self, nums: list[int]) -> int:
        pass