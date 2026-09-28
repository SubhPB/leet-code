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

        for i,height in enumerate(planks):
            # plank's height supposed as final height
            threshold=(height+1)//2
            width=cnt.get(height)
            for another_height in planks:
                if another_height>=threshold: 
                    break
                if height-another_height!=another_height:
                    width+=min(
                        cnt.get(another_height), cnt.get(height-another_height,0)
                    )
                else:
                    width+=cnt.get(another_height)//2
            res=max(res, width)

            # final height as sum of heights
            for j in range(i+1):
                height2=planks[j]
                full_height=height+height2
                threshold=(full_height+1)//2

                if height!=height2:
                    width=min(
                        cnt.get(height), cnt.get(height2)
                    )
                else: width//=2

                for another_height in planks:
                    if another_height>=threshold:
                        break
                    if another_height in (height2,height):
                        continue
                    
                    if full_height-another_height!=another_height:
                        width+=min(
                            cnt.get(another_height),
                            cnt.get(full_height-another_height,0)
                        )
                    else:
                        width+=cnt.get(another_height)//2
                res=max(res,width)

        return res
                    