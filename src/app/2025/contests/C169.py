from typing import List
class Solution:
    '''
    3737. Count Subarrays With Majority Element I
    You are given an integer array nums and an integer target.
    Return the number of subarrays of nums in which target is the majority element.
    The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

    Example 1:
    Input: nums = [1,2,2,3], target = 2
    Output: 5

    Explanation:
    Valid subarrays with target = 2 as the majority element:
    nums[1..1] = [2]
    nums[2..2] = [2]
    nums[1..2] = [2,2]
    nums[0..2] = [1,2,2]
    nums[1..3] = [2,2,3]
    So there are 5 such subarrays.

    Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 10​​​​​​^​9
    1 <= target <= 10^9
    '''
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums);total=nums.count(target);res=total
        fn=lambda x:0 if x!=target else 1;temp=fn(nums[0])
        for size in range(2,min(2*total,n+1)):
            temp+=fn(nums[size-1]); cnt=temp
            if cnt>size//2: res+=1
            for j in range(size,n):
                cnt+=fn(nums[j])-fn(nums[j-size])
                if cnt>size//2: res+=1
        return res
