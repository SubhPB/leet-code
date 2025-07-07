'''
    3585. Find Weighted Median Node in Tree

    You are given an integer n and an undirected, weighted tree rooted at node 0 with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates an edge from node ui to vi with weight wi.

    The weighted median node is defined as the first node x on the path from ui to vi such that the sum of edge weights from ui to x is greater than or equal to half of the total path weight.

    You are given a 2D integer array queries. For each queries[j] = [uj, vj], determine the weighted median node along the path from uj to vj.

    Return an array ans, where ans[j] is the node index of the weighted median for queries[j].

    Example 1:

    Input: n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]

    Output: [0,1]

    Explanation:

    Query	Path	Edge
    Weights	Total
    Path
    Weight	Half	Explanation	Answer
    [1, 0]	1 → 0	[7]	7	3.5	Sum from 1 → 0 = 7 >= 3.5, median is node 0.	0
    [0, 1]	0 → 1	[7]	7	3.5	Sum from 0 → 1 = 7 >= 3.5, median is node 1.	1
    Example 2:

    Input: n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]]

    Output: [1,0,2]

    Explanation:



    Query	Path	Edge
    Weights	Total
    Path
    Weight	Half	Explanation	Answer
    [0, 1]	0 → 1	[2]	2	1	Sum from 0 → 1 = 2 >= 1, median is node 1.	1
    [2, 0]	2 → 0	[4]	4	2	Sum from 2 → 0 = 4 >= 2, median is node 0.	0
    [1, 2]	1 → 0 → 2	[2, 4]	6	3	Sum from 1 → 0 = 2 < 3.
    Sum from 1 → 2 = 2 + 4 = 6 >= 3, median is node 2.	2
    Example 3:

    Input: n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]]

    Output: [2,2]

    Explanation:

    Query	Path	Edge
    Weights	Total
    Path
    Weight	Half	Explanation	Answer
    [3, 4]	3 → 1 → 0 → 2 → 4	[1, 2, 5, 3]	11	5.5	Sum from 3 → 1 = 1 < 5.5.
    Sum from 3 → 0 = 1 + 2 = 3 < 5.5.
    Sum from 3 → 2 = 1 + 2 + 5 = 8 >= 5.5, median is node 2.	2
    [1, 2]	1 → 0 → 2	[2, 5]	7	3.5	
    Sum from 1 → 0 = 2 < 3.5.
    Sum from 1 → 2 = 2 + 5 = 7 >= 3.5, median is node 2.

    2

    Constraints:

    2 <= n <= 10^5
    edges.length == n - 1
    edges[i] == [ui, vi, wi]
    0 <= ui, vi < n
    1 <= wi <= 109
    1 <= queries.length <= 10^5
    queries[j] == [uj, vj]
    0 <= uj, vj < n
    The input is generated such that edges represents a valid tree.

    python ./src/app/2025/July/3585.py
'''
from functools import cache
class Solution:
    def findMedian(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        lift, depth, rootDist = (n-1).bit_length(), [0]*n, [0]*n
        graph = [
            [] for _ in range(n)
        ]
        ancestors = [
            [-1]*n for _ in range(lift)
        ]
        for [u,v,w] in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        def dfs(u:int,parent:int):
            ancestors[0][u]=parent
            for [v,w] in graph[u]:
                if v != parent: 
                    depth[v] = depth[u]+1
                    rootDist[v] = rootDist[u]+w
                    dfs(v,u)
        dfs(0,-1)

        #Need to compute ancestor table
        for lft in range(1,lift):
            for u in range(n):
                parent = ancestors[lft-1][u]
                ancestors[lft][u] = ancestors[lft-1][parent]
        
        @cache
        def lca(u:int,v:int): 
            if depth[u] < depth[v]: u, v = v, u # ensure u is deepest
            #We'll try to match the depth level
            diff = depth[u]-depth[v]
            if diff>0:
                for lft in range(lift):
                    if (diff>>lft)&1: u = ancestors[lft][u]
            if u == v: return u
            while ancestors[0][u] != ancestors[0][v]:
                u = ancestors[0][u]
                v = ancestors[0][v]
            return ancestors[0][u] 
        
        def findDist(u:int,v:int):
            parent = lca(u,v) 
            return rootDist[u] + rootDist[v] - 2*rootDist[parent]

        @cache
        def findParent(lvl:int, node:int): # in case of lvl=0 node will point to itself!
            parent = node
            for i in range(lvl):
                if (lvl>>i)&1: parent = ancestors[i][parent]
            return parent
        
        def binarySearch(l:int,r:int,midCost:float,src:int,child:int):
            # 'l' and 'r' represents possible i-th parent of child which could be the 'median'
            ceil = 1 if r<l else 0 # 'ceil' works when v exist downwards not if when v exist upwards!
            if ceil: l,r = r,l
            while l<r:
                m = (l+r+ceil)//2
                parent = findParent(m, child)
                dist = float(findDist(src,parent))
                if dist > midCost:
                    if ceil: l = m
                    else: r = m
                elif dist < midCost:
                    if ceil: r = m-1
                    else: l = m+1
                else:
                    l,r = m,m
            return findParent(l, child) # median
        
        res = [0]*len(queries)
        for i, [u,v] in enumerate(queries):
            parent, midCost = lca(u,v), float(findDist(u,v)/2)
            if parent not in [u,v]: 
                l, r = 1, depth[u]-depth[parent]
                medianCost, child = float(findDist(u, parent)), u

                if medianCost < midCost:
                    l, r, child = depth[v]-depth[parent]-1, 0, v
                    
                res[i] = binarySearch(l,r,midCost,u,child)
            else:
                l, r, child = 1, depth[u]-depth[v], u

                if parent == u:
                    l, r, child = depth[v]-depth[u]-1, 0, v
                res[i] = binarySearch(l,r,midCost, u, child)
        return res
    
if __name__ == "__main__":
    testcases = []
    add = lambda n,edges,queries: testcases.append([n,edges,queries])

    add(n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]])
    add(n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]])
    add(n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]])

    sol = Solution()
    print('Running tests...\n')
    for [n,e,q] in testcases:
        print(f'n={n} edges={e} queries={q} result={sol.findMedian(n,e,q)}')