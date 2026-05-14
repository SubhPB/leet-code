class Solution:
    '''
    3909. Compare Sums of Bitonic Parts
    You are given a bitonic array nums of length n.
    Split the array into two parts:
    Ascending part: from index 0 to the peak element (inclusive).
    Descending part: from the peak element to index n - 1 (inclusive).
    The peak element belongs to both parts.
    Return:
    0 if the sum of the ascending part is greater.
    1 if the sum of the descending part is greater.
    -1 if both sums are equal.

    Example 1:
    Input: nums = [1,3,2,1]
    Output: 1

    Constraints:
    3 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    nums is a bitonic array.
    '''
    def compareBitonicSums(self, nums: list[int]) -> int:
        s=nums[0]; n=len(nums); p=s
        for i in range(1,n):
            p=max(p,nums[i])
            s+=nums[i]*[-1,1][int(nums[i]>nums[i-1])]
        s-=p
        if s!=0:
            return 0 if s>0 else 1
        return -1