from typing import List
class Solution:
    '''  
    3804. Number of Centered Subarrays
    You are given an integer array nums.
    A subarray of nums is called centered if the sum of its elements is equal to at least one element within that same subarray.
    Return the number of centered subarrays of nums.

    Example 1:
    Input: nums = [-1,1,0]
    Output: 5
    Explanation:
    All single-element subarrays ([-1], [1], [0]) are centered.
    The subarray [1, 0] has a sum of 1, which is present in the subarray.
    The subarray [-1, 1, 0] has a sum of 0, which is present in the subarray.
    Thus, the answer is 5.

    Constraints:
    1 <= nums.length <= 500
    -10^5 <= nums[i] <= 10^5
    '''
    def centeredSubarrays(self, nums: List[int]) -> int:
        n=len(nums);E=[0]*(n+1);res=0
        for i in range(n): E[i]+=E[i-1]+nums[i]
        print(f'E={E}')
        for l in range(n):
            for r in range(l,n):
                for x in range(l,r+1):
                    if nums[x]==E[r]-E[l-1]: 
                        res+=1; break

        return res