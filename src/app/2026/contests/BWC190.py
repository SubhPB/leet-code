class Solution:
    '''
    4035. Maximum Valid Split Positions I

    You are given an integer array nums.
    You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.
    A split position i of arr is valid if:

    0 <= i < m - 1, and
    gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
    An array of length 1 has no valid split positions.
    The score of arr is the number of valid split positions in it.
    Return the maximum possible score of arr.
    Here, gcd(a) denotes the greatest common divisor of all elements in the array a.

    Example 1:
    Input: nums = [10,30,15,10]
    Output: 2

    Constraints:
    2 <= nums.length <= 1000
    1 <= nums[i] <= 10**9​​​​​​​
    '''
    def maxValidSplits(self, nums: list[int]) -> int:
        pass