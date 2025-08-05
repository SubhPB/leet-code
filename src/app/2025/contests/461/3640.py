'''
3640. Trionic Array II

    You are given an integer array nums of length n.

    A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

    nums[l...p] is strictly increasing,
    nums[p...q] is strictly decreasing,
    nums[q...r] is strictly increasing.
    Return the maximum sum of any trionic subarray in nums.

    

    Example 1:

    Input: nums = [0,-2,-1,-3,0,2,-1]

    Output: -4

    Explanation:

    Pick l = 1, p = 2, q = 3, r = 5:

    nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
    nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
    nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
    Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.
    Example 2:

    Input: nums = [1,4,2,7]

    Output: 14

    Explanation:

    Pick l = 0, p = 1, q = 2, r = 3:

    nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
    nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
    nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
    Sum = 1 + 4 + 2 + 7 = 14.
    

    Constraints:

    4 <= n = nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    It is guaranteed that at least one trionic subarray exists.
    python ./src/app/2025/contests/461/3640.py
'''
from typing import List
from bisect import bisect_left
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums); res = -float('inf')

        Tn = [0]*(n+1); neg = [-1]
        for i in range(0,n):
            if nums[i]<0: neg.append(i)
            Tn[i+1] = Tn[i]+nums[i]

        def inc(i:int):
            while i<n and nums[i]<nums[min(n-1,i+1)]: i+=1
            return i
        def dec(i:int):
            while i<n and nums[i]>nums[min(n-1,i+1)]: i+=1
            return i
        
        l=0;p=0
        while n-p>=3:
            if l==p: 
                while l<n and nums[l]>=nums[min(n-1,l+1)]: l+=1
                p = inc(l)
            while l+1<p and nums[l]<0: l+=1 #If l starts with -ve value then try if we can neglect curr 'l'

            q = dec(p); r = inc(q)
            if l < p < q < r < n:
                seg1=Tn[p]-Tn[l]; seg2=Tn[q+1]-Tn[p]; seg3=Tn[r+1]-Tn[q+1]
                #maximize seg-1
                if nums[p]>0: 
                    i = neg[bisect_left(neg,p)-1]
                    while i>=l and i<l-1: 
                        seg1 = max(seg1, Tn[p]-Tn[i+1])
                        i = neg[bisect_left(neg,i)-1]
                else: seg1 = nums[p-1] # peak value is -ve, best to just take only one element
                #maximizing seg3        
                if nums[r]<0:
                    seg3 = nums[q+1] #better if we take only one element!
                else:
                    i = neg[bisect_left(neg,r)-1]
                    while i>q:
                        seg3 = max(seg3, Tn[i+1]-Tn[q+1])
                        i = neg[bisect_left(neg,i)-1]
                res = max(
                    res, seg1+seg2+seg3
                )
            l = q; p = r
        return res
    
if __name__ == '__main__':
    testcases = [
        [0,-2,-1,-3,0,2,-1],
        [-432,186,-568,390],
        [-434,332,-519,-175,917,-316,645]   
    ]
    for nums in testcases:
        print(f'Nums={nums} res={Solution().maxSumTrionic(nums)}')