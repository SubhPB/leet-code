class Solution:
    '''
    3905. Multi Source Flood Fill
    You are given two integers n and m representing the number of rows and columns of a grid, respectively.
    You are also given a 2D integer array sources, where sources[i] = [ri, ci, color​​​​​​​i] indicates that the cell (ri, ci) is initially colored with colori. All other cells are initially uncolored and represented as 0.
    At each time step, every currently colored cell spreads its color to all adjacent uncolored cells in the four directions: up, down, left, and right. All spreads happen simultaneously.
    If multiple colors reach the same uncolored cell at the same time step, the cell takes the color with the maximum value.
    The process continues until no more cells can be colored.
    Return a 2D integer array representing the final state of the grid, where each cell contains its final color.

    Example 1:
    Input: n = 3, m = 3, sources = [[0,0,1],[2,2,2]]
    Output: [[1,1,2],[1,2,2],[2,2,2]]

    Constraints:
    1 <= n, m <= 10**5
    1 <= n * m <= 10**5
    1 <= sources.length <= n * m
    sources[i] = [ri, ci, colori]
    0 <= ri <= n - 1
    0 <= ci <= m - 1
    1 <= colori <= 10**6​​​​​​​
    All (ri, ci​​​​​​​) in sources are distinct.
    '''
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key=lambda arg:-arg[2])
        g=[[0]*m for _ in range(n)]; i=0    
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]  
        while i<len(sources):
            [x,y,c]=sources[i]
            if not g[x][y]:
                g[x][y]=c
                for [ix,iy] in dirs:
                    nx=ix+x;ny=iy+y
                    if 0<=nx<n and 0<=ny<m and not g[nx][ny]:
                        sources.append([nx,ny,c])
            i+=1
        return g