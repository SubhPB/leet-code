from collections import deque
from typing import List

class Solution:
    '''
    You are given two integers numBottles and numExchange.
    numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:
    Drink any number of full water bottles turning them into empty bottles.
    Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
    Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

    Return the maximum number of water bottles you can drink.
    '''
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        while numBottles>=numExchange: #numBottles now represent emptyBottles
            numBottles-=numExchange
            numBottles+=1;numExchange+=1;res+=1
        return res
    '''
    407. Trapping Rain Water II

    Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

    Example 1:

    Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    Output: 4
    Explanation: After the rain, water is trapped between the blocks.
    We have two small ponds 1 and 3 units trapped.
    The total volume of water trapped is 4.
    
    Constraints:
        m == heightMap.length
        n == heightMap[i].length
        1 <= m, n <= 200
        0 <= heightMap[i][j] <= 2 * 10^4
    '''
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        maxHeight=0; ans=0; heights = set()
        m=len(heightMap); n=len(heightMap[0])

        for r in range(m):
            for c in range(n):
                h = heightMap[r][c]
                maxHeight = max(maxHeight,h)
                heights.add(h)

        # dummy value
        heightMap[m-1].append(0)

        def neighbors(x:int,y:int):
            N = []
            for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                r = x+i; c = y+j
                if 0<=r<m and 0<=c<n: 
                    N.append((r,c))
            if len(N) != 4: # dummy value
                N.append((m-1,n))
            return N

        for height in sorted(list(heights)):
            #Guarantee: minHeight among heightMap >= height
            traversed = set()
            for r in range(m):
                for c in range(n):
                    if height == heightMap[r][c] and (r,c) not in traversed:
                        q = deque([(r,c)]); rq = []
                        threshold = 2 * 10**4
                        while len(q):
                            currX,currY = q.popleft()
                            if (currX, currY) in traversed: continue
                            rq.append((currX,currY))
                            for x,y in neighbors(currX,currY):
                                if (x,y) in traversed: continue
                                ht = heightMap[x][y]
                                if ht == height and (x,y) != (m-1,n):
                                    q.append((x,y))
                                else: 
                                    threshold = min(threshold,ht)
                            traversed.add((currX,currY))
                        if threshold>height:
                            for nx,ny in rq:
                                ans += threshold-height
                                heightMap[nx][ny] = threshold
          
        return ans
    '''
    417. Pacific Atlantic Water Flow

    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Example 1:

    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
    [0,4]: [0,4] -> Pacific Ocean 
        [0,4] -> Atlantic Ocean
    [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
        [1,3] -> [1,4] -> Atlantic Ocean
    [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
        [1,4] -> Atlantic Ocean
    [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    [3,0]: [3,0] -> Pacific Ocean 
        [3,0] -> [4,0] -> Atlantic Ocean
    [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
        [3,1] -> [4,1] -> Atlantic Ocean
    [4,0]: [4,0] -> Pacific Ocean 
        [4,0] -> Atlantic Ocean
    Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

    Constraints:
        m == heights.length
        n == heights[r].length
        1 <= m, n <= 200
        0 <= heights[r][c] <= 10^5
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights);c=len(heights[0])
        pacific=set();altantic=set()

        def dfs(x:int,y:int,visit:set,prevHeight:int):
            if (0<=x<r and 0<=y<c) and (
                (x,y) not in visit
                ) and (heights[x][y]>=prevHeight):
                visit.add((x,y))
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr=x+i;ny=y+j
                    dfs(nr,ny,visit,heights[x][y])
        for col in range(c):
            dfs(0,col,pacific,heights[0][col])
            dfs(r-1,col,altantic,heights[r-1][col])
        for row in range(r):
            dfs(row,0,pacific,heights[row][0])
            dfs(row,c-1,altantic,heights[row][c-1])

        res=[]
        for row in range(r):
            for col in range(c):
                if (row,col) in pacific and (row,col) in altantic:
                    res.append([row,col])
        return res