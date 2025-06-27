'''
3553. Minimum Weighted Subgraph With the Required Paths II

You are given an undirected weighted tree with n nodes, numbered from 0 to n - 1. It is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an edge between nodes ui and vi with weight wi.​

Additionally, you are given a 2D integer array queries, where queries[j] = [src1j, src2j, destj].

Return an array answer of length equal to queries.length, where answer[j] is the minimum total weight of a subtree such that it is possible to reach destj from both src1j and src2j using edges in this subtree.

A subtree here is any connected subset of nodes and edges of the original tree forming a valid tree.

 

Example 1:

Input: edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]

Output: [12,11]

Explanation:

The blue edges represent one of the subtrees that yield the optimal answer.



answer[0]: The total weight of the selected subtree that ensures a path from src1 = 2 and src2 = 3 to dest = 4 is 3 + 5 + 4 = 12.

answer[1]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 2 to dest = 5 is 2 + 3 + 6 = 11.

Example 2:

Input: edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]

Output: [15]

Explanation:



answer[0]: The total weight of the selected subtree that ensures a path from src1 = 0 and src2 = 1 to dest = 2 is 8 + 7 = 15.
 

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 3
0 <= ui, vi < n
1 <= wi <= 104
1 <= queries.length <= 105
queries[j].length == 3
0 <= src1j, src2j, destj < n
src1j, src2j, and destj are pairwise distinct.
The input is generated such that edges represents a valid tree.
'''


class Solution:
    def minimumWeight(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        m, q = len(edges), len(queries)
        n = m+1

        depth, rootDist, graph = [0]*n, [0]*n, [[] for _ in range(n)]
        for [u,v,w] in edges:
            graph[u].append([v,w])
            graph[v].append([u,w])
        
        liftBound = (n-1).bit_length()
        ancestor = [
            [
                -1 for _ in range(n)
            ] for _ in range(liftBound)
        ] #ancestor[lift][node] = parent

        def dfs(node,parent):
            ancestor[0][node] = parent
            for [v,w] in graph[node]:
                if v!=parent:
                    depth[v] = depth[node]+1
                    rootDist[v] = rootDist[node]+w
                    dfs(v,node)
        dfs(0,-1)

        for lift in range(1,liftBound):
            for node in range(n):
                parent = ancestor[lift-1][node]
                ancestor[lift][node] = ancestor[lift-1][parent]
        
        def lca(u,v):
            if depth[u] < depth[v]: u,v = v,u
            diff = depth[u]-depth[v]
            if diff>0:
                for k in range(liftBound):
                    if (diff>>k)&1:
                        u = ancestor[k][u]
                    if u==v: return u
            # Till here u and v are at same depth
            while ancestor[0][u] != ancestor[0][v]:
                u = ancestor[0][u]
                v = ancestor[0][v]
            return ancestor[0][u]
        
        dist = lambda x,y: rootDist[x]+rootDist[y]-2*rootDist[lca(x,y)]

        res = [-1]*q
        for i in range(q):
            [u,v,d] = queries[i]
            res[i] = (
                dist(u,v) + dist(u,d) + dist(v,d)
            ) // 2
        return res