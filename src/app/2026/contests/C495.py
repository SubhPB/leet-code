
class Solution:
    '''
    3886. Sum of Sortable Integers

    You are given an integer array nums of length n.
    An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:
    Partition nums into consecutive subarrays of length k.
    Cyclically rotate each subarray independently any number of times to the left or to the right.
    Return an integer denoting the sum of all possible sortable integers k.

    Example 1:
    Input: nums = [3,1,2]
    Output: 3
    Explanation:​​​​​​​

    For n = 3, possible divisors are 1 and 3.
    For k = 1: each subarray has one element. No rotation can sort the array.
    For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
    Only k = 3 is sortable. Hence, the answer is 3.

    Constraints:
    1 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**5
    '''
    def sortableIntegers(self, nums: list[int]) -> int:
        pass