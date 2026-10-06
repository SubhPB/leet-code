class Solution:
    '''
    4011. Count Subarrays With Even Odd Ratio I

    You are given an integer array nums and two integers a and b.
    For a subarray, let:
    x be the number of even elements.
    y be the number of odd elements.
    The ratio of even to odd elements in a subarray is defined as x / y, where ratios are compared by their exact rational values.
    A subarray is considered valid if:
    y > 0, and
    x / y <= a / b.
    Return the number of valid subarrays in nums.

    Example 1:
    Input: nums = [1,2,1,2], a = 3, b = 2
    Output: 7

    Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
    1 <= a, b <= 1000
    '''
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        yt=0
        r=a/b
        res=0
        for i,num in enumerate(nums):
            yt+=num%2
            j=0; y=yt
            while j<=i and y>0:
                x=i-j+1-y
                if x/y <= r: res+=1
                y-=nums[j]%2
                j+=1
                    
        return res