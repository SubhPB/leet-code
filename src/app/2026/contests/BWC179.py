class Solution:
    '''
    3881. Direction Assignments with Exactly K Visible People
    You are given three integers n, pos, and k.
    There are n people standing in a line indexed from 0 to n - 1. Each person independently chooses a direction:
    'L': visible only to people on their right
    'R': visible only to people on their left
    A person at index pos sees others as follows:
    A person i < pos is visible if and only if they choose 'L'.
    A person i > pos is visible if and only if they choose 'R'.
    Return the number of possible direction assignments such that the person at index pos sees exactly k people.

    Since the answer may be large, return it modulo 109 + 7.
    
    Example 1:
    Input: n = 3, pos = 1, k = 0
    Output: 2
    Explanation:​​​​​​​
    Index 0 is to the left of pos = 1, and index 2 is to the right of pos = 1.
    To see k = 0 people, index 0 must choose 'R' and index 2 must choose 'L', keeping both invisible.
    The person at index 1 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2.

    Constraints:
    1 <= n <= 10^5
    0 <= pos, k <= n - 1
    '''
    def exp(self, i:int,mod:int):
        r=1; b=i; p=mod-2
        while p>0:
            if p%2: r=(r*b)%mod
            b=(b*b)%mod
            p>>=1
        return r
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod=10**9+7; u=1; b=1; k=min(k,n-1-k)
        for i in range(1,1+k):
            u=(u*(n-i))%mod
            b=(b*i)%mod
        return (2*(self.exp(b,mod)*u)%mod)%mod
    '''
    3882. Minimum XOR Path in a Grid

    You are given a 2D integer array grid of size m * n.
    You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
    At each step, you may move either right or down.
    The cost of a path is defined as the bitwise XOR of all the values in the cells along that path,
    including the start and end cells.
    Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

    Example 1:
    Input: grid = [[1,2],[3,4]]
    Output: 6
    Explanation:
    There are two valid paths:
    (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
    (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
    The minimum XOR value among all valid paths is 6.


    Constraints:
    1 <= m == grid.length <= 1000
    1 <= n == grid[i].length <= 1000
    m * n <= 1000
    0 <= grid[i][j] <= 1023​
    '''
    def minCost(self, grid: list[list[int]]) -> int:
        m=len(grid); n=len(grid[0])
        dp=[[[-1]*1024 for _ in range(n)] for _ in range(m)]
        def dfs(i:int,j:int,x:int):
            if i>=m or j>=n: return 1023
            x^=grid[i][j]
            if (i,j)==(m-1,n-1): return x
            elif dp[i][j][x]==-1:
                right=dfs(i,j+1,x)
                down=dfs(i+1,j,x)
                dp[i][j][x]=min(right,down)
            return dp[i][j][x]
        return dfs(0,0,0)
        