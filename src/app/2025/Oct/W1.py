from collections import deque
import heapq
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
    '''
    778. Swim in Rising Water

    You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
    It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.
    You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
    Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0). 

    Example 1:

    Input: grid = [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.
    Example 2:


    Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation: The final route is shown.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

    Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 50
    0 <= grid[i][j] < n2
    Each value grid[i][j] is unique.
    '''
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid); minDist=[[n**2+1]*n for _ in range(n)]
        h = [(grid[0][0],0,0)] # (dist,x,y)
        while h:
            d,x,y=heapq.heappop(h)
            if x==y==n-1: 
                return d
            elif d<minDist[x][y]:
                minDist[x][y]=d
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr=x+i;ny=y+j
                    if 0<=nr<n and 0<=ny<n:
                        nt=grid[nr][ny]; dt=max(0,nt-d)
                        heapq.heappush(h,(d+dt,nr,ny))
            
        return -1
    '''
    1488. Avoid Flood in The City

    Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

    Given an integer array rains where:

    rains[i] > 0 means there will be rains over the rains[i] lake.
    rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
    Return an array ans where:

    ans.length == rains.length
    ans[i] == -1 if rains[i] > 0.
    ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
    If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

    Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

    Example 1:

    Input: rains = [1,2,3,4]
    Output: [-1,-1,-1,-1]
    Explanation: After the first day full lakes are [1]
    After the second day full lakes are [1,2]
    After the third day full lakes are [1,2,3]
    After the fourth day full lakes are [1,2,3,4]
    There's no day to dry any lake and there is no flood in any lake.
    Example 2:

    Input: rains = [1,2,0,0,2,1]
    Output: [-1,-1,2,1,-1,-1]
    Explanation: After the first day full lakes are [1]
    After the second day full lakes are [1,2]
    After the third day, we dry lake 2. Full lakes are [1]
    After the fourth day, we dry lake 1. There is no full lakes.
    After the fifth day, full lakes are [2].
    After the sixth day, full lakes are [1,2].
    It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
    Example 3:

    Input: rains = [1,2,0,1,2]
    Output: []
    Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
    After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
    

    Constraints:

    1 <= rains.length <= 10^5
    0 <= rains[i] <= 10^9
    '''
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        res=[-1]*n; zeros = []

        sets=deque([])
        s=set(); stn=0
        for i in range(n):
            if not rains[i]:
                sets.appendleft(s)
                s=set()
                zeros.append(i)
            else:
                s.add(rains[i])
                stn+=1
        sets.appendleft(s)
        
        m=len(sets)
        if stn != n-m+1: return []

        for zeroat in zeros:
            s1=sets.pop(); s2=sets.pop()
            intersec = s1&s2; l = len(intersec)
            # print(f's1={s1} and s2={s2} intersec={intersec}')
            # Need to make two global sets! to resolve a specfic&major edgecase
            if l>1: return []
            res[zeroat] = intersec.pop() if l else 1
            sets.append(s1|s2)#safe-union
        
        return res