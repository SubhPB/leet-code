class Solution:
    '''
    3993. Maximum Value of an Alternating Sequence

    You are given three integers n, s, and m.
    A sequence seq of integers of length n is considered valid if:
    seq[0] = s.
    The sequence is alternating, meaning that either:
    seq[0] > seq[1] < seq[2] > ..., or
    seq[0] < seq[1] > seq[2] < ....
    For every adjacent pair, |seq[i] - seq[i - 1]| <= m.
    A sequence of length 1 is considered alternating.
    Return the maximum possible element that can appear in any valid sequence.

    Example 1:
    Input: n = 4, s = 3, m = 5
    Output: 12
    Explanation:
    One valid sequence is [3, 8, 7, 12].
    The maximum element in the sequence is 12.

    Constraints:
    1 <= n, s <= 10**9  
    1 <= m <= 10**5
    '''
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if not n-1: return s
        fn = lambda i:s - (i//2) + m*((i+1)//2 )
        return max(fn(n-1), fn(n-2)) 
    '''
    3994. Minimum Adjacent Swaps to Partition Array

    You are given an integer array nums and two integers a and b such that a < b.
    An array is called good if it can be split into three contiguous parts, in this order, such that:
    Every element in the first part is less than a.
    Every element in the second part is in the range [a, b] inclusive.
    Every element in the third part is greater than b.
    Any of the three parts may be empty.
    In one adjacent swap, you may swap two neighboring elements of nums.
    Return the minimum number of adjacent swaps required to make nums good. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:
    Input: nums = [1,3,2,4,5,6], a = 3, b = 4
    Output: 1
    Explanation:
    Swap nums[1] and nums[2]. The array becomes [1, 2, 3, 4, 5, 6].
    This array is good because it can be split into [1, 2], [3, 4], and [5, 6].

    Constraints:
    1 <= nums.length <= 10**5
    ​​​​​​​1 <= nums[i] <= 10**9
    1 <= a < b <= 10**9
    '''
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        pass