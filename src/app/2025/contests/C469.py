from typing import List

class Solution:
    '''
    3698. Split Array With Minimum Difference

    You are given an integer array nums.
    Split the array into exactly two subarrays, left and right, such that left is strictly increasing and right is strictly decreasing.
    Return the minimum possible absolute difference between the sums of left and right. If no valid split exists, return -1.

    Example 1:

    Input: nums = [1,3,2]

    Output: 2

    Explanation:

    i	left	right	Validity	left sum	right sum	Absolute difference
    0	[1]	[3, 2]	Yes	1	5	|1 - 5| = 4
    1	[1, 3]	[2]	Yes	4	2	|4 - 2| = 2
    Thus, the minimum absolute difference is 2.
    '''
    def splitArray(self, nums: List[int]) -> int:
        mx = max(nums)
        mxat = []; n = len(nums)
        for i in range(n):
            if nums[i] == mx: mxat.append(i)
        if len(mxat)>2: return -1
        # if n == len(mxat) == 2: return 0
        ls=0; rs=0
        for i in range(min(mxat[0],n-1)):
            if nums[i]<nums[i+1]:
                ls+=nums[i]
            else: break
        for j in range(mxat[-1]+1,n):
            if nums[j]>nums[j-1]: rs+=nums[j]
            else: return -1
        if len(mxat)==1:
            return abs(min(ls+mx-rs, ls-rs-mx))
        else: return abs(ls-rs)