class Solution:
    '''
    4015. Weighted Sum of a Tree

    You are given an integer array parent of length n representing a rooted tree with nodes labeled from 0 to n - 1.
    The tree is rooted at node 0, so parent[0] = -1. For each node i where 1 <= i <= n - 1, parent[i] denotes the parent of node i.
    You are also given an integer array nums of length n, where nums[i] denotes the value of node i.
    The weight of a node i at depth d is nums[i] * (h - d + 1), where h is the height of the tree.
    Return the sum of the weights of all nodes in the tree.
    The depth of a node is the number of nodes on the path from the root to that node, inclusive, with the root having depth 1.
    The height of the tree is the maximum depth among all nodes in the tree.

    Example 1:
    ​​​​​​
    Input: parent = [-1,0,0,0,2,2], nums = [5,2,3,1,4,6]
    Output: 37

    Constraints:
    1 <= n <= 10**5
    n == parent.length == nums.length
    parent[0] == -1
    0 <= parent[i] <= n - 1 for all i in [1, n - 1]
    1 <= nums[i] <= 10**6
    The input is generated such that the array parent represents a valid tree rooted at node 0.
    '''
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        pass
    '''
    4016. Maximum Area of Two Non-Overlapping Square Submatrices

    You are given a 2D integer matrix mat of size m × n, where:
    mat[r][c] == 1 means the cell at row r and column c is usable.
    mat[r][c] == 0 means it is not usable.
    Your task is to find two submatrices that satisfy the following conditions:
    Both submatrices must be squares of the same side length k.
    The two submatrices must not share any cell.
    Each submatrix can only cover cells where mat[r][c] == 1.
    Return the maximum possible area of each of the two squares. If it is not possible to choose two such squares, return 0.

    Example 1:
    Input: mat = [[1,1,1,0],[1,1,1,1],[0,0,1,1]]
    Output: 4
    Explanation:
    The largest equal non-overlapping squares have side length k = 2 with area 4.
    First square starts at top-left (0, 0) and covers cells (0, 0), (0, 1), (1, 0), and (1, 1).
    Second square starts at top-left (1, 2) and covers cells (1, 2), (1, 3), (2, 2), and (2, 3).
    Thus, the answer is 4.

    Constraints:
    mat.length == m
    mat[i].length == n
    1 <= m, n <= 500
    mat[i][j] is either 0 or 1.
    '''
    def maxArea(self, mat: list[list[int]]) -> int:
        pass