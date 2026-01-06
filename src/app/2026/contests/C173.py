from typing import List
class Solution:
    '''
    3795. Minimum Subarray Length With Distinct Sum At Least K
    You are given an integer array nums and an integer k.
    Return the minimum length of a subarray whose sum of the distinct values present in that subarray (each value counted once) is at least k. If no such subarray exists, return -1.
    
    Example 1:
    Input: nums = [2,2,3,1], k = 4
    Output: 2
    Explanation:
    The subarray [2, 3] has distinct elements {2, 3} whose sum is 2 + 3 = 5, which is ​​​​​​​at least k = 4. Thus, the answer is 2.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= k <= 10^9
    '''
    def minLength(self, nums: List[int], k: int) -> int:
        n=len(nums); res=n+1; s={}
        i=0;j=0;t=0
        while j<=n:
            if t>=k:
                res=min(res,j-i)
                s[nums[i]]-=1
                if not s[nums[i]]: 
                    del s[nums[i]]; t-=nums[i]
                i+=1
            else:
                if j<n:
                    if nums[j] not in s:
                        s[nums[j]]=0; t+=nums[j]
                    s[nums[j]]+=1
                j+=1
        return res if res<=n else -1