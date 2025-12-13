from typing import List

class Solution:
    '''
    3766. Minimum Operations to Make Binary Palindrome

    You are given an integer array nums.
    For each element nums[i], you may perform the following operations any number of times (including zero):
    Increase nums[i] by 1, or
    Decrease nums[i] by 1.
    A number is called a binary palindrome if its binary representation without leading zeros reads the same forward and backward.
    Your task is to return an integer array ans, where ans[i] represents the minimum number of operations required to convert nums[i] into a binary palindrome.

    Constraints:

    1 <= nums.length <= 5000
    ​​​​​​​1 <= nums[i] <= 5000
    '''
    def minOperations(self, inp: List[int]) -> List[int]:
        # --- Better to either cache or set into global scope
        nums=[0];x=1
        while nums[-1]<=5000:
            n=x.bit_length();m=(n+1)//2
            nums.append(x)
            for i in range(m):
                if bool(x&(1<<(n-i-1))) != bool(x&(1<<i)):
                    nums.pop(); break
            x+=1
        
        for i,num in enumerate(inp):
            l=0; r=len(nums)-1
            while l<r:
                m=(l+r+1)//2
                if nums[m]>num:
                    r=m-1
                else: l=m
            inp[i]=min(
                num-nums[l],
                nums[l+1]-num
            )
        return inp
    '''
    3767. Maximize Points After Choosing K Tasks

    You are given two integer arrays, technique1 and technique2, each of length n,
    where n represents the number of tasks to complete.
    If the ith task is completed using technique 1, you earn technique1[i] points.
    If it is completed using technique 2, you earn technique2[i] points.
    You are also given an integer k, representing the minimum number of tasks that must be completed using technique 1.
    You must complete at least k tasks using technique 1 (they do not need to be the first k tasks).
    The remaining tasks may be completed using either technique.
    Return an integer denoting the maximum total points you can earn.
    
    Example 1:
    Input: technique1 = [5,2,10], technique2 = [10,3,8], k = 2
    Output: 22
    Explanation:
    We must complete at least k = 2 tasks using technique1.
    Choosing technique1[1] and technique1[2] (completed using technique 1), and technique2[0] (completed using technique 2), yields the maximum points: 2 + 10 + 10 = 22.

    Constraints:

    1 <= n == technique1.length == technique2.length <= 105
    1 <= technique1[i], technique2​​​​​​​[i] <= 10​​​​​​​5
    0 <= k <= n
    '''
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        res=0; n=len(technique1); idxs=[]
        for i in range(n):
            if technique1[i]<technique2[i]:
                idxs.append(i) #technique1[i] wasn't selected!
            res+=max(technique1[i],technique2[i])
        m=len(idxs)
        if n-m<k:
            idxs.sort(key=lambda idx:technique2[idx]-technique1[idx])
            for i in range(k-n+m):
                res-=technique2[idxs[i]]-technique1[idxs[i]]
        return res
    '''
    3768. Minimum Inversion Count in Subarrays of Fixed Length
    You are given an integer array nums of length n and an integer k.
    An inversion is a pair of indices (i, j) from nums such that i < j and nums[i] > nums[j].
    The inversion count of a subarray is the number of inversions within it.
    Return the minimum inversion count among all subarrays of nums with length k.
    
    Example 1:
    Input: nums = [3,1,2,5,4], k = 3
    Output: 0
    Explanation:
    We consider all subarrays of length k = 3 (indices below are relative to each subarray):
    [3, 1, 2] has 2 inversions: (0, 1) and (0, 2).
    [1, 2, 5] has 0 inversions.
    [2, 5, 4] has 1 inversion: (1, 2).
    The minimum inversion count among all subarrays of length 3 is 0, achieved by subarray [1, 2, 5].

    Constraints:
    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= n
    '''
    def minInversionCount(self, nums: List[int], k: int) -> int:
        ln=[];i=0;n=len(nums)
        def left(num:int):
            nonlocal ln
            l=-1;r=len(ln)
            while l<r:
                m=(l+r+1)//2
                if ln[m]<num: l=m
                else: r=m-1
            return l
        def right(num:int):
            nonlocal ln
            l=0; r=len(ln)
            while l<r:
                m=(l+r)//2
                if ln[m]>num:
                    r=m
                else:
                    l=m+1
            return l
        temp=0
        while i<k:
            x=left(nums[i])
            ln=ln[:x+1]+[nums[i]]+ln[x+1:]
            temp+=x+1; i+=1
        res=temp
        for j in range(i,n):
            prev=nums[j-k]; x=left(prev)
            temp-=x+1;ln=ln[:x+1]+ln[x+2:]
            curr=nums[j]; y=right(curr)
            temp+=n-y; ln=ln[:y]+[curr]+ln[y:]

        return res