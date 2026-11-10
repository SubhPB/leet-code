class Solution:
    '''
    4039. Sum of Decoded Numbers

    You are given an integer array nums.
    Each nums[i] is an encoded integer representing two positive integers xi and yi. To decode nums[i], define:
    widthi = nums[i] % 10.
    di = floor(nums[i] / 10).
    xi as the integer formed by the first widthi digits of the decimal representation of di.
    yi as the integer formed by all remaining digits of the decimal representation of di.
    It is guaranteed that the decimal representation of di contains more than widthi digits. Therefore, both xi and yi contain at least one digit.
    The decoded value of nums[i] is xiyi.
    Return the sum of the decoded values of all elements in nums, modulo 109 + 7.
    The floor() function returns the integer part of the division.

    Example 1:
    Input: nums = [231]
    Output: 8
    Explanation:
    For 231, we have width = 1, d = 23, x = 2, and y = 3.
    The decoded value of 231 is 23 = 8.
    Since there is only one element in nums, the sum of the decoded values is 8.

    Constraints:
    1 <= nums.length <= 10**5
    100 < nums[i] < 10**15
    1 <= widthi <= 9
    1 <= xi, yi < 10**9
    The digit sequences used to form xi and yi do not have leading zeros.
    It is guaranteed that every element in nums is a valid encoded integer.
    '''
    def sumDecoded(self, nums: list[int]) -> int:
        pass