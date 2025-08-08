'''
3363. Find the Maximum Number of Fruits Collected
    There is a game dungeon comprised of n x n rooms arranged in a grid.

    You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

    The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

    The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
    The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
    The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
    When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

    Return the maximum number of fruits the children can collect from the dungeon.


    Example 1:

    Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]

    Output: 100

    Explanation:

    In this example:

    The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
    The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
    The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
    In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

    Example 2:

    Input: fruits = [[1,1],[1,1]]

    Output: 4

    Explanation:

    In this example:

    The 1st child moves on the path (0,0) -> (1,1).
    The 2nd child moves on the path (0,1) -> (1,1).
    The 3rd child moves on the path (1,0) -> (1,1).
    In total they collect 1 + 1 + 1 + 1 = 4 fruits.

    Constraints:

    2 <= n == fruits.length == fruits[i].length <= 1000
    0 <= fruits[i][j] <= 1000
'''
from typing import List
import heapq
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # (r,c) -> n*r + c
        n=len(fruits); res = sum([fruits[i][i] for i in range(n)])
        dist = [[0 for _ in range(n)] for _ in range(n)]
        p2Max = 0; p3Max=0

        Q = [(-fruits[0][n-1], 0, 0, n-1)]
        while Q:
            dt, st, r, c = heapq.heappop(Q); dt = -dt
            if (r,c)==(n-2,n-1): 
                p2Max = dt; break
            elif dt > dist[r][c] and c>r and st<n-1:
                dist[r][c]=dt
                for nc in [c+i for i in (-1,0,1)]:
                    nr = r+1
                    if nr<nc<n:
                        heapq.heappush(Q, (-dt-fruits[nr][nc],st+1,nr,nc))

        Q=[(-fruits[n-1][0], 0, n-1, 0)]
        while Q:
            dt, st, r, c = heapq.heappop(Q); dt=-dt
            if (r,c) == (n-1,n-2):
                p3Max=dt; break
            elif dt > dist[r][c] and c<r and st<n-1:
                dist[r][c]=dt
                for nr in [r+i for i in (-1,0,1)]:
                    nc = c+1
                    if nc<nr<n:
                        heapq.heappush(Q, (-dt-fruits[nr][nc],st+1,nr,nc))
                
        return res + p2Max + p3Max