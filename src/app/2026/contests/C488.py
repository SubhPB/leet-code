from typing import List
class Solution:
    '''
    3834. Merge Adjacent Equal Elements
    You are given an integer array nums.
    You must repeatedly apply the following merge operation until no more changes can be made:
    If any two adjacent elements are equal, choose the leftmost such adjacent pair in the current array and replace them with a single element equal to their sum.
    After each merge operation, the array size decreases by 1. Repeat the process on the updated array until no more changes can be made.
    Return the final array after all possible merge operations.
    
    Example 1:
    Input: nums = [3,1,1,2]
    Output: [3,4]
    Explanation:
    The middle two elements are equal and merged into 1 + 1 = 2, resulting in [3, 2, 2].
    The last two elements are equal and merged into 2 + 2 = 4, resulting in [3, 4].
    No adjacent equal elements remain. Thus, the answer is [3, 4].

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5​​​​​​​
    '''
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        n=len(nums);x=1;i=1
        while i<n:
            if nums[i]!=nums[x-1]:
                nums[x]=nums[i]; x+=1
            else:
                nums[x-1]*=2
            while x>1 and nums[x-1]==nums[x-2]:
                x-=1; nums[x-1]*=2
            i+=1
        return nums[:x]
    '''
    3835. Count Subarrays With Cost Less Than or Equal to K

    You are given an integer array nums, and an integer k.
    For any subarray nums[l..r], define its cost as:
    cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).
    Return an integer denoting the number of subarrays of nums whose cost is less than or equal to k.

    Example 1:
    Input: nums = [1,3,2], k = 4
    Output: 5
    Explanation:

    We consider all subarrays of nums:
    nums[0..0]: cost = (1 - 1) * 1 = 0
    nums[0..1]: cost = (3 - 1) * 2 = 4
    nums[0..2]: cost = (3 - 1) * 3 = 6
    nums[1..1]: cost = (3 - 3) * 1 = 0
    nums[1..2]: cost = (3 - 2) * 2 = 2
    nums[2..2]: cost = (2 - 2) * 1 = 0
    There are 5 subarrays whose cost is less than or equal to 4.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= k <= 10^15
    '''
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Solved something that was not asked!...
        n=len(nums); nums.append(0); res=0
        for i in range(n):
            nums[i]+=nums[i-1]
            if nums[i]-nums[i-1]<=k:
                l=0;r=i+1
                while l<r:
                    m=(l+r)//2; sk=nums[i]-nums[m-1]
                    if sk>k: l=m+1
                    else: r=m
                res+=((i-l+1)*(i-l+2))//2
        return res