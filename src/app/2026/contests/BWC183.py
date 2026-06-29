class Solution:
    '''
    3937. Minimum Operations to Make Array Modulo Alternating I

    You are given an integer array nums and an integer k.
    In one operation, you can increase or decrease any element of nums by 1.
    An array is called modulo alternating if there exist two distinct integers x and y (0 <= x, y < k) such that:
    For every even index i, nums[i] % k == x
    For every odd index i, nums[i] % k == y
    Return the minimum number of operations required to make nums modulo alternating.

    Example 1:
    Input: nums = [1,4,2,8], k = 3
    Output: 2
    Explanation:
    Let's choose x = 1 for even indices and y = 2 for odd indices.
    Perform the following operations:
    Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8].
    Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8].
    Now, for even indices, nums[i] % k = 1, and for odd indices, nums[i] % k = 2.
    Thus, the total number of operations required is 2.

    Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 10**9
    2 <= k <= 100
    '''
    def minOperations(self, nums: list[int], k: int) -> int:
        res=None; n=len(nums)
        for x in range(k):
            for y in range(x+1,k):
                temp1=0;temp2=0
                for i,num in enumerate(nums):
                    if i%2:
                        temp1+=min(k-x+num%k,k-num%k+x,abs(x-num%k))
                        temp2+=min(k-y+num%k,k-num%k+y,abs(y-num%k))
                    else:
                        temp2+=min(k-x+num%k,k-num%k+x,abs(x-num%k))
                        temp1+=min(k-y+num%k,k-num%k+y,abs(y-num%k))
                if res is None: res=temp1
                res=min(res,temp1,temp2)
        res = 0 if res is None else res
        return res 
    '''
    3938. Maximum Path Intersection Sum in a Grid

    You are given an m x n integer matrix grid.
    Two players move across the grid:
    Player 1 starts at the top-left cell (0, 0) and can move only right or down. Their destination is the bottom-right cell (m - 1, n - 1).
    Player 2 starts at the bottom-left cell (m - 1, 0) and can move only right or up. Their destination is the top-right cell (0, n - 1).
    Each player must choose a valid path from their respective starting cell to their destination.
    A cell is called shared if it belongs to both chosen paths.
    Return an integer denoting the maximum possible sum of values of all shared cells.
    Example 1:
    ​​​​​​​​​​​​​
    Input: grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]
    Output: 4

    Constraints:
    m == grid.length
    n == grid[i].length
    2 <= m, n <= 1000
    4 <= m * n <= 5 * 10**5
    -100 <= grid[i][j] <= 100
    '''
    def maxScore(self, grid: list[list[int]]) -> int:

        m=len(grid);n=len(grid[0]);res=-10**9
        for r in range(m):
            total=grid[r][0]
            least=0
            for c in range(1,n):
                least=min(least,total-grid[r][c-1])
                total+=grid[r][c]
                res=max(res,total-least)

        for c in range(n):
            total=grid[0][c]
            least=0
            for r in range(1,m):
                least=min(least,total-grid[r-1][c])
                total+=grid[r][c]
                res=max(res,total-least)
                
        if min(m,n)>2:
            for r in range(1,m-1):
                for c in range(1,n-1):
                    res=max(res,grid[r][c])
            
        return res