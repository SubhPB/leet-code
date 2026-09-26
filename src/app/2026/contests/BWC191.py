import math
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
    '''
    4050. Minimum Days to Score Exactly N Points

    You are given an integer n representing a target score.
    Your score starts at 0, and each day you either earn points or skip.
    Points are earned during a streak. On the first day of a streak you earn 1 point, on the second day 2 points,
    on the third day 3 points, and so on. Skipping a day earns nothing and resets the streak, so the next time you earn points,
    you start from 1 again.
    Return the minimum number of days, including any skipped days, needed to reach a score of exactly n.

    Example 1:
    Input: n = 2
    Output: 3

    Explanation:​​​​​​​
    Day 1: earn 1 point. Score is 1.
    Day 2: skip, which resets the streak. Earning here would add 2 points and take the score past n = 2.
    Day 3: the streak has reset, so earning gives 1 point. Score is exactly n = 2 in 3 days.

    Constraints:
    1 <= n <= 10**5
    '''
    def minDays(self, n: int) -> int:
        
        def bs(score:int):
            l=1; r=int(math.sqrt(score*2))
            while l<r:
                m=(l+r+1)//2
                if m*(m+1)<=score*2:
                    l=m
                else:
                    r=m-1
            return l   
        
        res=-1
        while n: #expception!!! 
            days=bs(n)
            n-=(days*(days+1))//2
            res+=days+1

        return res