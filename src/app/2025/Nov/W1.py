from typing import List

class Solution:
    '''
        2257. Count Unguarded Cells in the Grid

        You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
        A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
        Return the number of unoccupied cells that are not guarded.

        Example 1:

        Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
        Output: 7
        Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
        There are a total of 7 unguarded cells, so we return 7.
        Example 2:


        Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
        Output: 4
        Explanation: The unguarded cells are shown in green in the above diagram.
        There are a total of 4 unguarded cells, so we return 4.

        Constraints:

        1 <= m, n <= 10^5
        2 <= m * n <= 10^5
        1 <= guards.length, walls.length <= 5 * 10^4
        2 <= guards.length + walls.length <= m * n
        guards[i].length == walls[j].length == 2
        0 <= rowi, rowj < m
        0 <= coli, colj < n
        All the positions in guards and walls are unique.
    '''
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        res=m*n-len(guards)-len(walls); M=[[17]*n for _ in range(m)]
        for [r,c] in guards: M[r][c]=15
        for [r,c] in walls: M[r][c]=16
        for r in range(m):
            for c in range(n):
                if 0<M[r][c]<16: #Guard
                    if M[r][c]&1: #up eligible
                        up=r-1
                        while up>=0:
                            if 0<M[up][c]<16: #another guard
                                if M[up][c]&2: M[up][c]^=2
                                break
                            elif M[up][c]==16: #wall
                                break
                            else: #unguarded->guarded
                                res -= M[up][c]//17
                                M[up][c]=0
                            up-=1
                        M[r][c]^=1
                    if M[r][c]&2: #down eligible
                        down=r+1
                        while down<m:
                            if 0<M[down][c]<16:
                                if M[down][c]&1: M[down][c]^=1
                                break
                            elif M[down][c]==16:
                                break
                            else:
                                res-=M[down][c]//17
                                M[down][c]=0
                            down+=1
                        M[r][c]^=2
                    if M[r][c]&4: #left 
                        left=c-1
                        while left>=0:
                            if 0<M[r][left]<16:
                                if M[r][left]&8: M[r][left]^=8
                                break
                            elif M[r][left]==16:
                                break
                            else:
                                res-=M[r][left]//17
                                M[r][left]=0
                            left-=1
                        M[r][c]^=4
                    if M[r][c]&8: #right
                        right=c+1
                        while right<n:
                            if 0<M[r][right]<16:
                                if M[r][right]&4: M[r][right]^=4
                                break
                            elif M[r][right]==16:
                                break
                            else:
                                res-=M[r][right]//17
                                M[r][right]=0
                            right+=1
                        M[r][c]^=8
        return res