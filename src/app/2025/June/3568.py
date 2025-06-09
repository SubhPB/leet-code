'''
3568. Minimum Moves to Clean the Classroom

    You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

    'S': Starting position of the student
    'L': Litter that must be collected (once collected, the cell becomes empty)
    'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
    'X': Obstacle the student cannot pass through
    '.': Empty space
    You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

    Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

    Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

    

    Example 1:

    Input: classroom = ["S.", "XL"], energy = 2

    Output: 2

    Explanation:

    The student starts at cell (0, 0) with 2 units of energy.
    Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
    A valid sequence of moves to collect all litter is as follows:
    Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
    Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
    The student collects all the litter using 2 moves. Thus, the output is 2.
    Example 2:

    Input: classroom = ["LS", "RL"], energy = 4

    Output: 3

    Explanation:

    The student starts at cell (0, 1) with 4 units of energy.
    A valid sequence of moves to collect all litter is as follows:
    Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
    Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
    Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
    The student collects all the litter using 3 moves. Thus, the output is 3.
    Example 3:

    Input: classroom = ["L.S", "RXL"], energy = 3

    Output: -1

    Explanation:

    No valid path collects all 'L'.

    

    Constraints:

    1 <= m == classroom.length <= 20
    1 <= n == classroom[i].length <= 20
    classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
    1 <= energy <= 50
    There is exactly one 'S' in the grid.
    There are at most 10 'L' cells in the grid.
'''

import heapq, math

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m,n = len(classroom), len(classroom[0])
        
        pq = []
        ix, iy = 0, 0
        idx, lcnt = {}, 0 #idx and lcnt will help to track "L" as in mask

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    ix, iy = i, j
                elif classroom[i][j] == 'L':
                    idx[(i,j)]=lcnt
                    lcnt+=1
       
        def setelem(x, y, steps, e, mask):
            heapq.heappush(pq, (steps, e, mask, x, y))
        def popelem():
            (steps, e, mask, x, y) = heapq.heappop(pq)
            return (x, y, steps, e, mask)


        dp = [ #dp[x][y][mask]: the most energy found at this spot
            [
               [
                    -math.inf for msk in range(2**lcnt)
               ] for j in range(n)
            ] for i in range(m)
        ]

        def isvalid(x,y): return 0<=x<m and 0<=y<n and classroom[x][y]!='X'
        def validpaths(x,y):
            res=[]
            for i,j in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                if isvalid(x+i, y+j): res.append((x+i,y+j))
            return res
        
        setelem(ix, iy, 0, energy, 0)
        while len(pq):
            x, y, steps, e, mask = popelem()
            if mask == (2**lcnt)-1: return steps
            elif not e or e <= dp[x][y][mask]: continue
            dp[x][y][mask] = e

            for nx, ny in validpaths(x,y):
                nextmask = mask
                if classroom[nx][ny] == "L":
                    offset = idx[(nx,ny)]
                    visited = mask&(1<<offset)
                    if not visited: nextmask = mask|(1<<offset)
                    
                setelem(
                    nx,
                    ny,
                    steps+1,
                    energy if classroom[nx][ny]=="R" else e-1 ,
                    nextmask
                )

        return -1