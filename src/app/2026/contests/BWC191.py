class Solution:
    '''
    4049. Count Values With Equally Spaced Occurrences II

    You are given an integer array nums.
    An integer x is called special if:
    x appears at least three times in nums.
    All occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices i1 < i2 < ... < im, then i2 - i1 = i3 - i2 = ... = im - im-1.
    Return the number of distinct special integers in nums.

    Example 1:
    Input: nums = [1,8,1,5,1,5,8,5]
    Output: 2
    Explanation:
    1 is special because it occurs at equally spaced indices 0, 2, and 4.
    5 is special because it occurs at equally spaced indices 3, 5, and 7.
    8 is not special because it occurs only twice.
    Therefore, the answer is 2.


    Constraints:
    3 <= nums.length <= 10**5
    1 <= nums[i] <= 10**9
    '''
    def countSpecialIntegers(self, nums: list[int]) -> int:
        diff={}; cnt={}; prev={}
        for i,num in enumerate(nums):
            curr_cnt=cnt.get(num,0)
            if curr_cnt:
                curr_diff=i-prev[num]
                if num not in diff:
                    diff[num]=curr_diff
                else:
                    if curr_diff!=diff[num]:
                        diff[num]=-1
            cnt[num]=1+curr_cnt
            prev[num]=i
        res=0
        for num in cnt:
            if cnt[num]>=3 and diff[num]!=-1:
                res+=1
        return res