'''
    1931. Painting a Grid With Three Different Colors
    You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

    Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

    Example 1:

    Input: m = 1, n = 1
    Output: 3
    Explanation: The three possible colorings are shown in the image above.
    Example 2:

    Input: m = 1, n = 2
    Output: 6
    Explanation: The six possible colorings are shown in the image above.
    Example 3:

    Input: m = 5, n = 5
    Output: 580986
    
    Constraints:

    1 <= m <= 5
    1 <= n <= 1000

    python ./src/app/2025/July/1931.py
'''

class Solution:
    def __init__(self):
        max_cols, col_bits  = 1000, 1<<2*5
        self.state = [
            [-1 for _ in range(max_cols)] for _ in range(col_bits)
        ]

    def colorTheGrid(self, m: int, n: int) -> int:
        M = 10**9+7
        add = lambda x,y:(x%M + y%M)%M
        def count_ways(r:int,c:int,curr:int,prev:int):
            if c==n: return 1
            elif not r and self.state[c][prev]!=-1: return self.state[c][prev]
            ways = 0
            nr = (r+1)%m
            up, left = curr&3, (prev>>2*(m-r-1))&3 if prev else 0
            for col in range(1,4):
                if col not in [up,left]:
                    nCurr = (curr<<2) | col
                    if nr:
                        ways = add(
                            ways, count_ways(nr,c,nCurr,prev)
                        )
                    else:
                        ways = add(
                            ways, count_ways(nr,c+1,0,nCurr)
                        )
            if not r and c: self.state[c][prev]=ways
            return ways
        return count_ways(0,0,0,0)
if __name__ == "__main__":
    sol = Solution()
    testcases =[
        [1,1],[1,2],[5,5]
    ]
    for [m,n] in testcases:
        print(f'm={m} n={n} count={sol.colorTheGrid(m,n)}')