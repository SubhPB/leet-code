from typing import List

class Solution:
    '''
    3740. Minimum Distance Between Three Equal Elements I
    You are given an integer array nums.
    A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
    The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
    Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

    Example 1:
    Input: nums = [1,2,1,1,3]
    Output: 6

    Explanation:
    The minimum distance is achieved by the good tuple (0, 2, 3).
    (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

    Constraints:
    1 <= n == nums.length <= 100
    1 <= nums[i] <= n
    '''
    def minimumDistance(self, nums: List[int]) -> int:
        inf=10**9;res=inf;freq={}
        for i,num in enumerate(nums):
            if num not in freq: freq[num]=[]
            if len(freq[num])<2: freq[num].append(i)
            else: 
                [a,b]=freq[num]
                res=min(res, (i-a)*2)
                freq[num]=[b,i]
        if res==inf: res=-1
        return res