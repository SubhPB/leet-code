class Solution:
    '''
    3862. Find the Smallest Balanced Index
    You are given an integer array nums.
    An index i is balanced if the sum of elements strictly to the left of i equals the product of elements strictly to the right of i.
    If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.
    Return an integer denoting the smallest balanced index. If no balanced index exists, return -1.

    Example 1:
    Input: nums = [2,1,2]
    Output: 1

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    '''
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        γ=-1;Σ=sum(nums);Π=1;x=10**18;n=len(nums)
        for i in range(n-1,-1,-1):
            Σ-=nums[i]
            if Σ==Π:γ=i
            Π*=nums[i]
            if Π>x: break
        return γ