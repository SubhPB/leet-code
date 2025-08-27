'''
    3459. Length of Longest V-Shaped Diagonal Segment

    You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

    A V-shaped diagonal segment is defined as:

    The segment starts with 1.
    The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
    The segment:
    Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
    Continues the sequence in the same diagonal direction.
    Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


    Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

    Example 1:

    Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

    Output: 5

    Explanation:

    The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

    Example 2:

    Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

    Output: 4

    Explanation:
shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

    Example 3:

    Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

    Output: 5

    Explanation:

    The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

    Example 4:

    Input: grid = [[1]]

    Output: 1

    Explanation:

    The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

    
    Constraints:

    n == grid.length
    m == grid[i].length
    1 <= n, m <= 500
    grid[i][j] is either 0, 1 or 2.
'''
from typing import List
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        res=0; m=len(grid); n=len(grid[0])

        init = lambda: [[1]*n for _ in range(m)]
        TL,TR,BR,BL = (init() for _ in range(4))

        # calc BR & BL
        for x in range(m-2,-1,-1):
            for y in range(n-1,-1,-1):
                z = grid[x][y]
                if z!=1:
                    # BR
                    if y!=n-1 and grid[x+1][y+1] not in [1,z]:
                        BR[x][y] += BR[x+1][y+1]
                    # BL
                    if y!=0 and grid[x+1][y-1] not in [1,z]:
                        BL[x][y] += BL[x+1][y-1]
        # calc TL & TR
        for x in range(1,m):
            for y in range(n):
                z=grid[x][y]
                if z!=1:
                    # TL
                    if y!=0 and grid[x-1][y-1] not in [1,z]:
                        TL[x][y] += grid[x-1][y-1]
                    # TR
                    if y!=n-1 and grid[x-1][y+1] not in [1,z]:
                        TR[x][y] += grid[x-1][y+1]

        for x in range(m):
            for y in range(n):
                z = grid[m][n]
                if z==1:
                    tempRes = 1; delta = 0
                    # TL
                    if x!=0 and y!=0 and grid[x-1][y-1] != 1:
                        tl = TL[x-1][y-1]; tempRes += tl
                        nx = x-tl; ny=y-tl
                        # what would happen if we do 90-degree turn? means TR from grid[x-p][y-p]
                        if nx!=0 and grid[nx-1][ny+1] != 1:
                            delta = max(delta, TR[nx-1][ny+1])
                    # TR
                    if x!=0 and y!=n-1 and grid[x-1][y+1] != 1:
                        tr = TR[x+1][y+1]; tempRes += tr
                        nx = x-tr; ny=y+tr
                        if ny!=n-1 and nx!=m-1 and grid[nx+1][ny-1] != 1:
                            delta = max(delta, BL[nx+1][ny-1])
                    # BR
                    # if x!=m-1 and y!=n-1 and grid[x]
                        
                        



        return res
    