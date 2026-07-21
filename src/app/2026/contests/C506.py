class Solution:
    '''
    3960. Frequency Balance Subarray

    You are given an integer array ​​​​​​​nums.
    Define a frequency balance subarray as follows:
    If the subarray contains only one distinct value, it is frequency balanced.
    Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times, and both frequencies occur among the distinct values.
    Return an integer denoting the length of the longest frequency balance subarray.

    Example 1:
    Input: nums = [1,2,2,1,2,3,3,3]
    Output: 5
    Explanation:
    The longest frequency balance subarray is [2, 1, 2, 3, 3].
    The elements that appear most frequently are 2 and 3, both appearing twice.
    The remaining element 1 appears once, meeting the requirements.

    Constraints:
    1 <= nums.length <= 10**​​​​​​​3
    1 <= nums[i] <= 10**​​​​​​​9
    '''
    def getLength(self, nums: list[int]) -> int:
        pass