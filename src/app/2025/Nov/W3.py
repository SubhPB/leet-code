from typing import List
class Solution:
    '''
    2435. Paths in Matrix Whose Sum Is Divisible by K

    You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.
    Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:

    Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
    Output: 2
    Explanation: There are two paths where the sum of the elements on the path is divisible by k.
    The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
    The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

    Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 5 * 10^4
    1 <= m * n <= 5 * 10^4
    0 <= grid[i][j] <= 100
    1 <= k <= 50
    '''
    def numberOfPaths(self, G: List[List[int]], k: int) -> int:
        m,n=len(G),len(G[0]);mod=10**9+7
        plus=lambda x,y: (x%mod+y%mod)%mod
        dp=[[[0]*k for _ in range(n)] for __ in range(m)]
        dp[m-1][n-1][(k-G[m-1][n-1]%k)%k]=1
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if (r,c)==(m-1,n-1): continue
                elif 0<=r<m and 0<=c<n:
                    for e in range(k):
                        en=(e+G[r][c])%k
                        if r!=m-1 and c!=n-1:
                            dp[r][c][e]=plus(dp[r+1][c][en],dp[r][c+1][en])
                        elif r==m-1:
                            dp[r][c][e]=dp[r][c+1][en]
                        else: 
                            dp[r][c][e]=dp[r+1][c][en]
        return dp[0][0][0]