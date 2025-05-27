'''
1857. Largest Color Value in a Directed Graph

    There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

    You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

    Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

    Example 1:

    Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
    Output: 3
    Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
    Example 2:

    Input: colors = "a", edges = [[0,0]]
    Output: -1
    Explanation: There is a cycle from 0 to 0.
    

    Constraints:

    n == colors.length
    m == edges.length
    1 <= n <= 105
    0 <= m <= 105
    colors consists of lowercase English letters.
    0 <= aj, bj < n
'''

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]

        for u, v in edges: graph[u].append(v)

        dp = [ [0]*n for _ in range(26) ]

        max_col_len = 0

        UNVISITED, PROCESSING, VISITED = [i for i in range(3)]
        state = [UNVISITED]*n

        #DFS
        def dfs(node:int):
            if state[node] == PROCESSING: return -1#Cycle detected

            if state[node] == UNVISITED:

                state[node] = PROCESSING
                for v in graph[node]:
                    res = dfs(v)
                    if res == -1: return -1

                    for i in range(26):
                        dp[i][node] = max(
                            dp[i][node],
                            dp[i][v]
                        )
                dp[ord(colors[node])-97][node] += 1
                state[node] = VISITED
            return dp[ord(colors[node])-97][node]
        #DFS.

        for i in range(n):
            res = dfs(node=i)
            if res == -1: return -1
            max_col_len = max(
                max_col_len,
                res
            )
        return max_col_len
