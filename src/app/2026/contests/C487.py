from typing import List
class Solution:
    '''
    3828. Final Element After Subarray Deletions

    You are given an integer array nums.
    Two players, Alice and Bob, play a game in turns, with Alice playing first.
    In each turn, the current player chooses any subarray nums[l..r] such that r - l + 1 < m, where m is the current length of the array.
    The selected subarray is removed, and the remaining elements are concatenated to form the new array.
    The game continues until only one element remains.
    Alice aims to maximize the final element, while Bob aims to minimize it. Assuming both play optimally, return the value of the final remaining element.

    Example 1:
    Input: nums = [1,5,2]
    Output: 2
    Explanation:
    One valid optimal strategy:
    Alice removes [1], array becomes [5, 2].

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    '''
    def finalElement(self, nums: List[int]) -> int:
        l=0;r=len(nums)-1;t=1
        while l<r:
            mxi=l;mni=l
            for i in range(l,r+1):
                if nums[mxi]<=nums[i]:mxi=i
                if nums[mni]>=nums[i]:mni=i
            if mxi==mni: break
            if t%2: #Alice's turn
                if mni<mxi: l=mxi
                else: r=mxi
            else: #Bob's turn
                if mni<mxi: r=mni
                else: l=mni
            t+=1
        return nums[l]
    '''
    3830. Longest Alternating Subarray After Removing At Most One Element

    You are given an integer array nums.

    A subarray nums[l..r] is alternating if one of the following holds:

    nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...
    nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...
    In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between strictly greater and strictly smaller.
    You can remove at most one element from nums. Then, you select an alternating subarray from nums.
    Return an integer denoting the maximum length of the alternating subarray you can select.
    A subarray of length 1 is considered alternating.

    Example 1:
    Input: nums = [2,1,3,2]
    Output: 4
    Explanation:
    Choose not to remove elements.
    Select the entire array [2, 1, 3, 2], which is alternating because 2 > 1 < 3 > 2.

    Constraints:
    2 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    '''
    def longestAlternating(self, nums: List[int]) -> int:
        n=len(nums); tk=[1]*n
        if nums[0]!=nums[1]: tk[1]=2
        for i in range(2,n):
            [e1,e2,e3]=[nums[i-x] for x in range(3)]
            if e1<e2>e3 or e1>e2<e3: tk[i]+=tk[i-1]
            elif e2!=e1: tk[i]+=1
        res=max(tk); tk[n-1]=1; tk[n-2]=1
        if nums[n-1]!=nums[n-2]: tk[n-2]=2
        for i in range(n-3,0,-1):
            [e1,e2,e3]=[nums[i+x] for x in range(3)]
            if (nums[i-1]>e2<e3 or nums[i-1]<e2>e3): res=max(
                res, tk[i]+tk[i+1]-1
            )
            if e1<e2>e3 or e1>e2<e3: tk[i]=tk[i+1]+1
            elif e1!=e2: tk[i]=2
            else: tk[i]=1
        return res