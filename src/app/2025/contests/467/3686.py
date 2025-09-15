'''
3686. Number of Stable Subsequences

    You are given an integer array nums.

    A subsequence is stable if it does not contain three consecutive elements with the same parity when the subsequence is read in order (i.e., consecutive inside the subsequence).

    Return the number of stable subsequences.

    Since the answer may be too large, return it modulo 109 + 7.

    

    Example 1:

    Input: nums = [1,3,5]

    Output: 6

    Explanation:

    Stable subsequences are [1], [3], [5], [1, 3], [1, 5], and [3, 5].
    Subsequence [1, 3, 5] is not stable because it contains three consecutive odd numbers. Thus, the answer is 6.
    Example 2:

    Input: nums = [2,3,4,2]

    Output: 14

    Explanation:

    The only subsequence that is not stable is [2, 4, 2], which contains three consecutive even numbers.
    All other subsequences are stable. Thus, the answer is 14.
    

    Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10​​​​​​^​5
'''
from typing import List
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        n = len(nums); hsh = [0]*n
        for i,num in enumerate(nums):
            hsh[i]=hsh[max(0,i-1)]
            if not num&1: hsh[i]+=1
        res = 0; M = 10**9+7
        add = lambda x,y: (x%M + y%M)%M
        for l in range(n-2):
            for r in range(l+2,n):
                x = sum([nums[i]&1 for i in (l,r)])
                d = hsh[r]-hsh[l]
                if x == 2:
                    res = add(res, d)
                elif x == 1:
                    res = add(res, r-l-1) # relax by 1
                else: #-> 0
                    res = add(res, r-l-d)
        return res