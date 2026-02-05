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