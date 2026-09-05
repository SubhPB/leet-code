class Solution:
    '''
    3987. Minimum Total Cost to Process All Elements

    You are given an integer array nums and an integer k.
    Initially, you have k units of resources.
    You must process the elements of nums from left to right. To process the ith element, you need nums[i] resources.
    If your available resources are less than nums[i], you may perform an operation that increases your available resources by k. The value of k is fixed and does not change throughout the process.
    The first such operation incurs a cost of 1, the second incurs a cost of 2, and so on.
    After processing the ith element, your available resources decrease by nums[i].
    Return an integer denoting the minimum total cost required to process all elements. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:
    Input: nums = [1,2,3,4], k = 4
    Output: 3
    Explanation:
    After processing nums[0], we have 4 - 1 = 3 units of resources left.
    After processing nums[1], we have 3 - 2 = 1 unit of resources left.
    Since nums[2] = 3 and only 1 unit of resources is available, we perform the first operation costing 1. After processing nums[2], we have 1 + 4 - 3 = 2 units of resources left.
    Since nums[3] = 4 and only 2 units of resources are available, we perform the second operation costing 2, to have 2 + 4 = 6 units of resources, which is enough to process nums[3].
    Thus, the total cost is 1 + 2 = 3.

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**9
    1 <= k <= 10**9
    '''
    def minimumCost(self, nums: list[int], k: int) -> int:
        mod=10**9+7
        rsrc=k
        ops=0
        mul=lambda x,y: (x%mod*y%mod)%mod
        add=lambda x,y: (x%mod+y%mod)%mod
        for num in nums:
            if num>rsrc:
                f=(num-rsrc+k-1)//k
                ops=add(ops,f)
                rsrc=add(rsrc, mul(f,k))
            rsrc-=num
        return mul(ops,ops+1)//2
    '''
    3988. Create Grid With Exactly K Paths I

    You are given three integers m, n, and k.
    Construct any m x n grid consisting only of the characters '.' and '#', where:
    '.' represents a free cell.
    '#' represents an obstacle cell.
    A valid path is a sequence of free cells that:
    Starts at the top-left cell (0, 0).
    Ends at the bottom-right cell (m - 1, n - 1).
    Moves only:
    Right, from (i, j) to (i, j + 1), or
    Down, from (i, j) to (i + 1, j).
    Return any grid such that there are exactly k valid paths from the top-left cell to the bottom-right cell.
    If no such grid exists, return an empty array.

    Example 1:
    Input: m = 2, n = 3, k = 2
    Output: ["...","#.."]
    Explanation:
    There are exactly k = 2 valid paths from (0, 0) to (1, 2):
    (0, 0) → (0, 1) → (0, 2) → (1, 2)
    (0, 0) → (0, 1) → (1, 1) → (1, 2)

    Constraints:
    1 <= m, n <= 10
    1 <= k <= 4
    '''
    def createGrid(self, m: int, n: int, k: int) -> list[str]: 
        temp=[
            [],
            [['.']],
            [['..', '..']],
            [['..', '..', '..'], ['...', '...']],
            [['..','..','..','..'], ['....','....'], ['..#','...','#..']]
        ]
        for t in temp[k]:
            r,c=len(t), len(t[0])
            if r<=m and c<=n:
                res=[
                    ['#']*n for _ in range(m)
                ]
                for i in range(r):
                    for j in range(c):
                        res[i][j]=t[i][j]
                for i in range(r,m):
                    res[i][c-1]='.'
                for j in range(c,n):
                    res[m-1][j]='.'
                return [''.join(row) for row in res]

        return []
    '''
    3989. Maximum Consistent Columns in a Grid
    You are given a 2D integer array grid of size m x n, and an integer limit.
    You may remove zero or more columns from the grid, but at least one column must remain. The relative order of the remaining columns must be preserved.
    A grid is called consistent if for every row i, and for every pair of adjacent remaining columns a and b with a < b, the following holds: |grid[i][b] - grid[i][a]| <= limit.
    Return the maximum number of columns that can remain such that the resulting grid is consistent.

    Example 1:
    Input: grid = [[-2,0,3]], limit = 2
    Output: 2
    Explanation:
    Remove column 2 and keep columns 0 and 1, which gives |grid[0][1] − grid[0][0]| = |0 − (−2)| = 2 <= limit.
    Thus, the maximum number of columns that can remain is 2.
 
    Constraints:
    1 <= m == grid.length <= 250
    1 <= n == grid[i].length <= 250
    -105 <= grid[i][j] <= 10**5
    0 <= limit <= 10**5
    '''
    def maxConsistentColumns(self, grid: list[list[int]], limit: int) -> int:
        pass