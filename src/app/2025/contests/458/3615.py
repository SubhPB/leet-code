'''
    3615. Longest Palindromic Path in Graph

    You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1 and a 2D array edges,
    where edges[i] = [ui, vi] indicates an edge between nodes ui and vi.

    You are also given a string label of length n, where label[i] is the character associated with node i.
    You may start at any node and move to any adjacent node, visiting each node at most once.
    Return the maximum possible length of a palindrome that can be formed by visiting a set of unique nodes along a valid path.

    Example 1:

    Input: n = 3, edges = [[0,1],[1,2]], label = "aba"

    Output: 3

    Explanation:
    The longest palindromic path is from node 0 to node 2 via node 1, following the path 0 → 1 → 2 forming string "aba".
    This is a valid palindrome of length 3.
    Example 2:

    Input: n = 3, edges = [[0,1],[0,2]], label = "abc"

    Output: 1

    Explanation:
    No path with more than one node forms a palindrome.
    The best option is any single node, giving a palindrome of length 1.
    Example 3:

    Input: n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac"

    Output: 3

    Explanation:
    The longest palindromic path is from node 0 to node 1, following the path 0 → 3 → 1, forming string "bcb".
    This is a valid palindrome of length 3.
    

    Constraints:

    1 <= n <= 14
    n - 1 <= edges.length <= n * (n - 1) / 2
    edges[i] == [ui, vi]
    0 <= ui, vi <= n - 1
    ui != vi
    label.length == n
    label consists of lowercase English letters.
    There are no duplicate edges.

    python ./src/app/2025/contests/458/3615.py
'''
class Solution:
    def maxLen(self, n: int, edges: list[list[int]], label: str) -> int:
        dp = [
            [
                [-1]*n for _ in range(n)
            ] for _ in range(1<<n)
        ]
        graph = [[] for _ in range(n)]
        for [u,v] in edges: 
            graph[u].append(v)
            graph[v].append(u)

        def dfs(mask:int,u:int,v:int):
            if dp[mask][u][v]>=0: return dp[mask][u][v]
            pairs = 0
            for a in graph[u]:
                if mask&(1<<a): continue
                for b in graph[v]:
                    if a==b or mask&(1<<b) or label[a] != label[b]: continue
                    newMask = mask | 1<<a | 1<<b
                    pairs = max(
                        pairs, 1+dfs(newMask, a, b)
                    )
            dp[mask][u][v] = pairs
            dp[mask][v][u] = pairs
            return pairs
        
        best = 1
        
        #odd-length palindrome
        for node in range(n):
            mask = 1<<node; pairs = dfs(mask,node,node)
            best = max(best, 1+2*pairs)
        
        #even-length palindrome
        for [u,v] in edges:
            if label[u]==label[v]:
                mask = 1<<u|1<<v; pairs = dfs(mask,u,v)
                best = max(
                    best, 2*(1+pairs)
                )

        return best
        
                       
            
        
if __name__ == '__main__':
    testcases = []
    add = lambda n,edges,label:testcases.append([n,edges,label])

    add(n = 3, edges = [[0,1],[1,2]], label = "aba")
    add(n = 3, edges = [[0,1],[0,2]], label = "abc")
    add(n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac")
    add(n=3,edges=[[1,0],[2,1],[0,2]], label="hjj")
    add(n=5,edges=[[4,3],[2,1],[2,4],[0,3],[3,1],[3,2]],label="bbeaa")

    for [n,edges,label] in testcases:
        print(f'n={n} edges={edges} label={label} maxLen={Solution().maxLen(n,edges,label)}')