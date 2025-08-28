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

        GET = lambda x,y,T:  T[x][y] if 0<=x<m and 0<=y<n and grid[x][y] != 1 else 0


        for x in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                if grid[x][y]!=1:
                    if GET(x+1,y+1,BR) and grid[x+1][y+1]!=grid[x][y]:
                        BR[x][y] += GET(x+1,y+1,BR)
                    if GET(x+1,y-1,BL) and grid[x+1][y-1] != grid[x][y]:
                        BL[x][y] += GET(x+1,y-1,BL)
                else:
                    BR[x][y] = GET(x+1,y+1,BR)
                    BL[x][y] = GET(x+1,y-1,BL)

        for x in range(m):
            for y in range(n):
                if grid[x][y]!=1:
                    if GET(x-1,y-1,TL) and grid[x-1][y-1] != grid[x][y]:
                        TL[x][y] += GET(x-1,y-1,TL)
                    if GET(x-1,y+1,TR) and grid[x-1][y+1] != grid[x][y]:
                        TR[x][y] += GET(x-1,y+1,TR)
                else:
                    TL[x][y] = GET(x-1,y-1,TL)
                    TR[x][y] = GET(x-1,y+1,TR)


        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    delta = 0; tempRes = 1

                    tl = TL[x][y]; tempRes+=tl; v = GET(x-tl,y-tl,TR)
                    if tl: delta = max(delta, v-max(0,v-1))

                    tr = TR[x][y]; tempRes+=tr; v = GET(x-tr, y+tr, BR)
                    if tr: delta = max(delta, v-max(0,v-1))

                    br = BR[x][y]; tempRes+=br; v = GET(x+br, y+br, BL)
                    if br: delta = max(delta, v-max(0,v-1))

                    bl =BL[x][y]; tempRes+=bl; v = GET(x+bl,y-bl,TL)
                    if bl: delta = max(delta, v-max(0,v-1))

                    res = max(res, tempRes+delta)

        return res
    