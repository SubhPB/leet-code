from typing import List
class Solution:
    '''
    3732. Maximum Product of Three Elements After One Replacement

    You are given an integer array nums.

    You must replace exactly one element in the array with any integer value in the range [-105, 105] (inclusive).

    After performing this single replacement, determine the maximum possible product of any three elements at distinct indices from the modified array.

    Return an integer denoting the maximum product achievable.

    

    Example 1:
    Input: nums = [-5,7,0]
    Output: 3500000
    Explanation:
    Replacing 0 with -105 gives the array [-5, 7, -105], which has a product (-5) * 7 * (-105) = 3500000. The maximum product is 3500000.

    Example 2:
    Input: nums = [-4,-2,-1,-3]
    Output: 1200000
    Explanation:
    Two ways to achieve the maximum product include:
    [-4, -2, -3] → replace -2 with 105 → product = (-4) * 105 * (-3) = 1200000.
    [-4, -1, -3] → replace -1 with 105 → product = (-4) * 105 * (-3) = 1200000.
    The maximum product is 1200000.

    Constraints:

    3 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
    '''
    def maxProduct(self, nums: List[int]) -> int:
        a=-10**5;b=int(a)
        for num in nums:
            b=max(b,abs(num))
            if a<b: a,b=b,a
        return (10**5)*a*b
    '''
    3733. Minimum Time to Complete All Deliveries

    You are given two integer arrays of size 2: d = [d1, d2] and r = [r1, r2].
    Two delivery drones are tasked with completing a specific number of deliveries. Drone i must complete di deliveries.
    Each delivery takes exactly one hour and only one drone can make a delivery at any given hour.
    Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone i must recharge every ri hours (i.e. at hours that are multiples of ri).
    Return an integer denoting the minimum total time (in hours) required to complete all deliveries.

    Example 1:
    Input: d = [3,1], r = [2,3]
    Output: 5
    Explanation:
    The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4).
    The second drone delivers at hour 2 (recharges at hour 3).

    Constraints:
    d = [d1, d2]
    1 <= di <= 10^9
    r = [r1, r2]
    2 <= ri <= 3 * 10^4
    '''
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        pass