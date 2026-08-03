from math import floor, log10
class Solution:
    '''
    3969. Valid Subarrays With Matching Sum Digits I
    You are given an integer array nums and an integer digit x.
    A subarray nums[l..r] is considered valid if the sum of its elements satisfies both of the following conditions:
    The first digit of the sum is equal to x.
    The last digit of the sum is equal to x.
    Return the number of valid subarrays.

    Example 1:
    Input: nums = [1,100,1], x = 1
    Output: 4
    Explanation:
    The valid subarrays are:
    nums[0..0]: sum = 1
    nums[0..1]: sum = 1 + 100 = 101
    nums[1..2]: sum = 100 + 1 = 101
    nums[2..2]: sum = 1
    Thus, the answer is 4.

    Constraints:
    1 <= nums.length <= 1500
    1 <= nums[i] <= 109
    1 <= x <= 9
    '''
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        res=0;n=len(nums);nums.append(0)
        length= lambda val: floor(log10(val))+1
        for i in range(1,n):
            nums[i]+=nums[i-1]
        for l in range(1,n+1):
            for i in range(n-l+1):
                sm=nums[i+l-1]-nums[i-1]
                pw=length(sm)-1
                if x==sm//(10**pw)==sm%10:
                    res+=1
        return res

