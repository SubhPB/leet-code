class Solution:
    '''
    4044. Count Good Cyclic Rotations

    You are given an integer array nums of even length n.
    A cyclic rotation of nums is obtained by choosing a prefix of nums whose length is between 0 and n - 1 (inclusive), and moving it to the end of the array while preserving the order of all elements.
    A cyclic rotation is good if the sum of its first n / 2 elements is strictly greater than the sum of its last n / 2 elements.
    Return the number of cyclic rotations of nums that are good.

    Example 1:
    Input: nums = [1,2,3,4,5,6]

    Output: 3

    Constraints:
    2 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    n is even.
    '''
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        total=sum(nums)
        res=n//2
        curr=0
        for i in range(n//2):
            curr+=nums[i]
        for i in range(n//2,n):
            if curr*2==total:
                res-=1
            curr-=nums[i-n//2]
            curr+=nums[i]
        return res

    '''
    4045. Count Robot Groups

    You are given a strictly increasing integer array position, where position[i] is the initial position of the ith robot at time t = 0.
    You are also given an integer array speed, where speed[i] is the constant speed of the ith robot in units per second, and an integer distance.
    Time is continuous and measured in seconds. A robot or group with speed v moves v * t units to the right over any interval of t seconds.
    Whenever the distance between two robots or groups becomes at most distance, they merge into a single group.
    If multiple robots or groups satisfy the merging condition at the same time, all merges happen simultaneously.
    In particular, every connected collection of robots or groups whose consecutive positions differ by at most distance merges into one group.
    After a merge, the resulting group takes the current position and speed of the rightmost robot in that group. Once merged, robots never separate.
    Return the number of groups remaining after all possible merges have occurred.
    
    Example 1:
    Input: position = [1,5,6,20], speed = [4,3,2,3], distance = 1
    Output: 2

    Explanation:
    Initially, the groups are {R1}, {R2}, {R3}, and {R​​​​​​​4}.
    At t = 0, the robots R2 and R3 at positions 5 and 6, respectively, merge because they are 1 unit apart.
    The resulting group moves with the position and speed of the rightmost robot R3. The groups are now {R1}, {R2, R3}, and {R​4}.
    Later at t = 2, the robot R1 catches up to the group {R2, R3} and merges with it. The groups are now {R1, R2, R3} and {R​4}.
    Thus, the answer is 2.

    Constraints:
    1 <= position.length == speed.length <= 10***5
    1 <= position[i], speed[i], distance <= 10**9
    position is strictly increasing.
    '''
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        pass
    '''
    4046. Minimum Cost Path With At Most K Turns

    You are given a 2D integer array grid of size m x n, where grid[i][j] represents the cost of visiting cell (i, j), and an integer k.
    You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
    From each cell, you may move one step in any of the four directions: up, down, left, or right.
    The cost of a path is the sum of the values of all visited cells, including the starting and ending cells.
    If a cell is visited more than once, its value is included each time it is visited.
    Return the minimum possible path cost to reach (m - 1, n - 1) using at most k turns. If no such path exists, return -1.
    A turn occurs when the direction changes between two consecutive moves. For example, moving right and then down counts as one turn,
    while moving right and then right does not.

    Example 1:
    Input: grid = [[2,7,3],[1,4,5]], k = 1
    Output: 12

    Constraints:
    1 <= m == grid.length <= 75
    1 <= n == grid[i].length <= 75
    0 <= grid[i][j] <= 1000
    0 <= k < min(m, n)
    '''
    def minCost(self, grid: list[list[int]], k: int) -> int:
        pass