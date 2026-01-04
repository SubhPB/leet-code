'''------------#1411------------'''
M=10**9+7; N=5001
MUL=lambda x,y: (x%M*y%M)%M
ADD = lambda x,y: (x%M+y%M)%M
transform = lambda d,u: [
    ADD(MUL(3,d),MUL(2,u)),
    ADD(MUL(2,d),MUL(2,u))
]
cache=[[6,6] for _ in range(N)]; cache[0]=[0,0]
for n in range(2,N): cache[n]=transform(*cache[n-1])
'''------------#1411------------'''

class Solution:
    '''
    1411. Number of Ways to Paint N × 3 Grid

    You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors:
    Red, Yellow, or Green while making sure that no two adjacent cells have the same color 
    (i.e., no two cells that share vertical or horizontal sides have the same color).
    Given n the number of rows of the grid, return the number of ways you can paint this grid.
    As the answer may grow large, the answer must be computed modulo 109 + 7.

    Example 1:
    Input: n = 1
    Output: 12
    Explanation: There are 12 possible way to paint the grid as shown.
    Example 2:

    Input: n = 5000
    Output: 30228214

    Constraints:
    n == grid.length
    1 <= n <= 5000
    '''
    def numOfWays(self, n: int) -> int:
        return ADD(*cache[n])
