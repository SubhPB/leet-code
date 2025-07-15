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
'''

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD, state = 10**9+7, [
            [-1 for _ in range(1<<2*m)] for _ in range(n)
        ]
        def count_ways(r:int,c:int,curr:int,prev:int):
            nonlocal MOD, state
            if c==n: return 1
            elif r==0 and state[c][prev]!=-1: return state[c][prev]
            ways, up_color =  0, curr&(3<<2*(r-1))
            for color in range(1,4):
                left_color = prev&(3<<2*r)
                if color not in [up_color, left_color]:
                    diff = (r+1)//m
                    nxt_r, nxt_c = (r+1)%m, c+diff
                    nxt_curr, nxt_prev = [curr|(color<<(2*r+1)), 0][diff], [prev,curr][diff]
                    ways = (
                        ways%MOD + count_ways(nxt_r, nxt_c, nxt_curr, nxt_prev)%MOD
                    )%MOD
            if r==0: state[c][prev]=ways
            return ways
        return count_ways(0,0,0,0)