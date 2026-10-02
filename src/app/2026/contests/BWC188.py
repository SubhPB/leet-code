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
    '''
    4008. Minimum Initial Strength to Defeat All Monsters
    You are given an integer array monsters, where monsters[i] represents the strength of the ith monster.
    You are also given a 2D integer array boosts, where boosts[i] = [li, ri, vi] indicates that vi is added to your temporary bonus
    while fighting any monster whose index lies in [li, ri]. Boost ranges may overlap, and the values of all applicable boosts are added together.
    You start with a non-negative initial strength and fight the monsters from left to right.
    For each monster at index i:
    Let bonus be the sum of the values of all boosts that apply to monster i.
    You can defeat the monster only if your current strength plus bonus is at least monsters[i].
    After defeating the monster, only your current strength decreases by monsters[i]. If it becomes negative, it is set to 0.
    Return the minimum initial strength required to defeat all monsters.
    Note: The temporary bonus is used only to determine whether the current monster can be defeated. It does not otherwise change your current strength.

    Example 1:
    Input: monsters = [5,10,15], boosts = [[1,1,10]]
    Output: 30
    Explanation:
    Let's start with an initial strength of 30.
    monsters[0] = 5: At index 0, the bonus is 0. Since 30 + 0 >= 5, this monster can be defeated. The strength becomes 30 - 5 = 25.
    monsters[1] = 10: At index 1, the bonus is 10. Since 25 + 10 >= 10, this monster can be defeated. The strength becomes 25 - 10 = 15.
    monsters[2] = 15: At index 2, the bonus is 0. Since 15 + 0 >= 15, this monster can be defeated. The strength becomes 15 - 15 = 0.
    Thus, the minimum initial strength required is 30.

    Constraints:
    1 <= monsters.length <= 5 * 10**4
    1 <= monsters[i] <= 10**9
    0 <= boosts.length <= 5 * 10**4
    boosts[i] == [li, ri, vi]
    0 <= li <= ri < monsters.length
    1 <= vi <= 10**9​​​​​​​
    '''
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n=len(monsters)
        nums=[0]*(n+1)
        for [l,r,v] in boosts:
            nums[l]+=v
            nums[r+1]-=v
        l=0;r=sum(monsters)
        def go(val:int):
            boost=0
            for i in range(n):
                boost+=nums[i]
                if val+boost<monsters[i]:
                    return False
                val=max(val-monsters[i],0)
            return True
        while l<r:
            m=(l+r)//2
            if go(m):
                r=m
            else:
                l=m+1
        return l