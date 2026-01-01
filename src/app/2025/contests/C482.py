from typing import List
class Solution:
    '''
    3788. Maximum Score of a Split

    You are given an integer array nums of length n.
    Choose an index i such that 0 <= i < n - 1.
    For a chosen split index i:
    Let prefixSum(i) be the sum of nums[0] + nums[1] + ... + nums[i].
    Let suffixMin(i) be the minimum value among nums[i + 1], nums[i + 2], ..., nums[n - 1].
    The score of a split at index i is defined as:
    score(i) = prefixSum(i) - suffixMin(i)
    Return an integer denoting the maximum score over all valid split indices.

    Example 1:
    Input: nums = [10,-1,3,-4,-5]
    Output: 17
    Explanation:
    The optimal split is at i = 2, score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17.

    Constraints:
    2 <= nums.length <= 10^5
    -109​​​​​​​ <= nums[i] <= 10^9
    '''
    def maximumScore(self, nums: List[int]) -> int:
        res=None; n=len(nums); t=0; mins=[nums[-1]]*n
        for i in range(n-2,-1,-1): mins[i]=min(nums[i],mins[i+1])
        for i in range(n-1):
            t+=nums[i]
            res=t-mins[i+1] if res is None else max(res,t-mins[i+1])
        return res
    '''
    3789. Minimum Cost to Acquire Required Items

    You are given five integers cost1, cost2, costBoth, need1, and need2.
    There are three types of items available:

    An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
    An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
    An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.
    You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.

    Return an integer representing the minimum possible total cost to achieve these requirements.


    Example 1:
    Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2
    Output: 3
    Explanation:

    After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
    Any other valid combination would cost more, so the minimum total cost is 3.

    Constraints:

    1 <= cost1, cost2, costBoth <= 10^6
    0 <= need1, need2 <= 10^9
    '''
    def minimumCost(self, c1: int, c2: int, cb: int, n1: int, n2: int) -> int:
        fn=lambda x:max(0,x)
        return min(
            c1*n1+c2*n2,
            cb*n1+fn(n2-n1)*c2,
            cb*n2+fn(n1-n2)*c1
        )
    '''
    3790. Smallest All-Ones Multiple
    You are given a positive integer k.
    Find the smallest integer n divisible by k that consists of only the digit 1 in its decimal representation (e.g., 1, 11, 111, ...).
    Return an integer denoting the number of digits in the decimal representation of n. If no such n exists, return -1.

    Example 1:
    Input: k = 3
    Output: 3
    Explanation:
    n = 111 because 111 is divisible by 3, but 1 and 11 are not. The length of n = 111 is 3.

    Constraints:
    2 <= k <= 10^5
    '''
    def minAllOneMultiple(self, k: int) -> int:
        mods=[0]*k; n=1; x=1
        while k%2:
            m=n%k
            if not m: return x
            if mods[m]: return -1
            mods[m]=1; n=m*10+1; x+=1
        return -1