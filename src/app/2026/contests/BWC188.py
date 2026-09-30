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
        heights={}
        planks=list(set(planks))
        for i,height in enumerate(planks):
            heights[height]=heights.get(height,0)+cnt[height]
            for j in range(i):
                height2=planks[j]
                full_height=height+height2
                heights[full_height] = heights.get(full_height,0) + min(
                    cnt[height], cnt[height2]
                )
            heights[2*height]=heights.get(2*height,0)+cnt.get(height,0)//2

        return max([heights[height] for height in heights])

                    