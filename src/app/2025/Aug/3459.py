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

        init = lambda: [[0]*n for _ in range(m)]
        TL,TR,BR,BL = (init() for _ in range(4))

        # TL/TR
        for x in range(m):
            for y in range(n):
                if grid[x][y]!=1:
                    TL[x][y] = 1; TR[x][y] = 1
                    nx=x-1; ny=y-1
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != grid[x][y]:
                        TL[x][y]+=TL[nx][ny]
                    nx=x-1; ny=y+1
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != grid[x][y]:
                        TR[x][y]+=TR[nx][ny]
        # BR/BL
        for x in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                if grid[x][y]!=1:
                    BR[x][y]=1; BL[x][y]=1
                    nx=x+1; ny=y-1
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != grid[x][y]:
                        BL[x][y]+=BL[nx][ny]
                    nx=x+1; ny = y+1
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != grid[x][y]:
                        BR[x][y]+=BR[nx][ny]
        
        TS = [TL,TR,BR,BL]; dirs = [(-1,-1),(-1,1),(1,1),(1,-1)]
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    values:List[tuple] = []
                    for i in range(4):
                        ix,iy = dirs[i]; T = TS[i]
                        nx=x+ix; ny=y+iy
                        dirMax = 0; z=0 # if this dir will sure use the  
                        while 0<=nx<m and 0<=ny<n and T[x+iy][y+iy]>z:
                            dirMax = max(dirMax, z+TS[(i+1)%4][nx][ny])
                            nx+=ix; ny+=iy; z+=1
                        values.append((z,dirMax))# (default,valueAfter90deg)
                    
                    defaultSums = sum([d for d,_ in values])
                    for default, dirMax in values:
                        res = max(
                            res,
                            defaultSums-default+dirMax+1
                        )
                        
        return res
    