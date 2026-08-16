class Solution:
    '''
    3979. Maximum Valid Pair Sum
    You are given an integer array nums of length n and an integer k.
    A pair of indices (i, j) is called valid if:
    0 <= i < j < n
    j - i >= k
    Return the maximum value of nums[i] + nums[j] among all valid pairs.

    Example 1:
    Input: nums = [1,3,5,2,8], k = 2
    Output: 13

    Constraints:
    2 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    1 <= k <= n - 1
    '''
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n=len(nums); mxr=[0]*n; res=0
        for i,num in enumerate(nums):
            mxr[i]=max(mxr[i-1],num)
        for j in range(n-1,k-1,-1):
            res=max(res,nums[j]+mxr[j-k])
        return res