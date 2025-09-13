'''
3623. Count Number of Trapezoids I

    You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

    A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

    Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

    Since the answer may be very large, return it modulo 109 + 7.

    Example 1:

    Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

    Output: 3

    Explanation:

    There are three distinct ways to pick four points that form a horizontal trapezoid:

    Using points [1,0], [2,0], [3,2], and [2,2].
    Using points [2,0], [3,0], [3,2], and [2,2].
    Using points [1,0], [3,0], [3,2], and [2,2].
    Example 2:

    Input: points = [[0,0],[1,0],[0,1],[2,1]]

    Output: 1

    Explanation:

    There is only one horizontal trapezoid that can be formed.

    Constraints:

    4 <= points.length <= 10^5
    –10^8 <= xi, yi <= 10^8
    All points are pairwise distinct.
'''
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points.sort(key=lambda z:z[1])
        res, adjs, currY = 0, [0], points[0][1]
        
        for [_,y] in points:
            if y!=currY:
                currY = y; adjs.append(0)
            adjs[-1]+=1

        M = 10**9+7
        add = lambda a,b:(a%M+b%M)%M
        mul = lambda a,b:(a%M*b%M)%M
        linearProgression = lambda n: mul(n,n+1)//2

        progressionSum = linearProgression(adjs[0]-1)
        for i in range(1,len(adjs)):
            cnt = adjs[i]
            currSum = linearProgression(cnt-1)
            res = add(res, mul(currSum, progressionSum))
            progressionSum = add(progressionSum, currSum) 
                
                
        return res
        
        
