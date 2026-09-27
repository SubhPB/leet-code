from collections import Counter
class Solution:
    '''
    4007. Widest Possible Fence

    You are given an integer array planks, where planks[i] represents the height of the ith wooden plank. Each plank has a width of 1 unit.
    You want to build a fence consisting of planks that all have the same height
    You may either use a plank as is,
    or combine exactly two distinct original planks into a single plank whose height equals the sum of their heights.
    Each original plank can be used at most once, and not all original planks need to be used.
    Return the maximum possible width of the fence that can be built.

    Example 1:
    Input: planks = [1,3,2,5,7,5,4,2,1]
    Output: 4

    Constraints:
    1 <= planks.length <= 1000
    1 <= planks[i] <= 10**9
    '''
    def maximumWidth(self, planks: list[int]) -> int:
        cnt=Counter(planks)
        planks=list(set(planks))
        planks.sort()
        res=0
        for p in planks:
            temp=cnt.get(p)
            x=(p+1)//2 
            for d in planks:
                if d>=x: break
                temp+=min(cnt.get(d,0), cnt.get(p-d,0))
            res=max(res,temp)
        return res