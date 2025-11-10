from typing import List

class Solution:
    '''
    3740. Minimum Distance Between Three Equal Elements I
    You are given an integer array nums.
    A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
    The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
    Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

    Example 1:
    Input: nums = [1,2,1,1,3]
    Output: 6

    Explanation:
    The minimum distance is achieved by the good tuple (0, 2, 3).
    (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

    Constraints:
    1 <= n == nums.length <= 100
    1 <= nums[i] <= n
    '''
    def minimumDistance(self, nums: List[int]) -> int:
        inf=10**9;res=inf;freq={}
        for i,num in enumerate(nums):
            if num not in freq: freq[num]=[]
            if len(freq[num])<2: freq[num].append(i)
            else: 
                [a,b]=freq[num]
                res=min(res, (i-a)*2)
                freq[num]=[b,i]
        if res==inf: res=-1
        return res
    
    '''
    3742. Maximum Path Score in a Grid

    You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.
    You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.
    Each cell contributes a specific score and incurs an associated cost, according to their cell values:
    0: adds 0 to your score and costs 0.
    1: adds 1 to your score and costs 1.
    2: adds 2 to your score and costs 1. ​​​​​​​
    Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.
    Note: If you reach the last cell but the total cost exceeds k, the path is invalid. 

    Example 1:
    Input: grid = [[0, 1],[2, 0]], k = 1
    Output: 2

    Constraints:
    1 <= m, n <= 200
    0 <= k <= 10^3​​​​​​​
    ​​​​​​​grid[0][0] == 0
    0 <= grid[i][j] <= 2
    '''
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m=len(grid);n=len(grid[0]);res=-1

        #@cache needed!
        def dfs(r:int,c:int,score:int,left:int):
            nonlocal res
            if r<m and c<n:
                score+=grid[r][c]
                left-=min(1,grid[r][c])
                if left>=0: 
                    if (r,c)==(m-1,n-1):
                        res=max(res,score)
                    else:
                        dfs(r+1,c,score,left)
                        dfs(r,c+1,score,left)
        dfs(0,0,0,k)
        return res