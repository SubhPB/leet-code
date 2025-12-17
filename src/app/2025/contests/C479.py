from typing import List
class Solution:
    '''
    3771. Total Score of Dungeon Runs
    You are given a positive integer hp and two positive 1-indexed integer arrays damage and requirement.
    There is a dungeon with n trap rooms numbered from 1 to n. Entering room i reduces your health points by damage[i]. After that reduction, if your remaining health points are at least requirement[i], you earn 1 point for that room.
    Let score(j) be the number of points you get if you start with hp health points and enter the rooms j, j + 1, ..., n in this order.
    Return the integer score(1) + score(2) + ... + score(n), the sum of scores over all starting rooms.
    Note: You cannot skip rooms. You can finish your journey even if your health points become non-positive.

    

    Example 1:
    Input: hp = 11, damage = [3,6,7], requirement = [4,2,5]
    Output: 3

    Explanation:
    score(1) = 2, score(2) = 1, score(3) = 0. The total score is 2 + 1 + 0 = 3.

    As an example, score(1) = 2 because you get 2 points if you start from room 1.

    You start with 11 health points.
    Enter room 1. Your health points are now 11 - 3 = 8. You get 1 point because 8 >= 4.
    Enter room 2. Your health points are now 8 - 6 = 2. You get 1 point because 2 >= 2.

    Constraints:

    1 <= hp <= 10^9
    1 <= n == damage.length == requirement.length <= 10^5
    1 <= damage[i], requirement[i] <= 10^4
    '''
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n=len(damage);res=0
        i,j,p=n-1,n-1,0
        while i>=0:
            # print(f'({i},{j}) hp:{hp}->thishp:{hp-damage[i]} nowp:{p} nowres={res} bool:{hp-damage[i]>=requirement[i]}')

            hp-=damage[i]
            if hp>=requirement[i]:
                i-=1; p+=1; res+=p
            elif hp>=0:
                i-=1; res+=p
            else: # hp:-ve
                hp+=damage[i]
                if i!=j: hp+=damage[j]
                if damage[j]<=requirement[j]: p-=1
                j-=1
            i=min(i,j)
        return res