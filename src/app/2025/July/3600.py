'''
3600. Maximize Spanning Tree Stability with Upgrades
    You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:

    ui and vi indicates an undirected edge between nodes ui and vi.
    si is the strength of the edge.
    musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.
    You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.

    The stability of a spanning tree is defined as the minimum strength score among all edges included in it.

    Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.

    Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.
    

    Example 1:

    Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1

    Output: 2

    Explanation:

    Edge [0,1] with strength = 2 must be included in the spanning tree.
    Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
    The resulting spanning tree includes these two edges with strengths 2 and 6.
    The minimum strength in the spanning tree is 2, which is the maximum possible stability.
    Example 2:

    Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2

    Output: 6

    Explanation:

    Since all edges are optional and up to k = 2 upgrades are allowed.
    Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
    The resulting spanning tree includes these two edges with strengths 8 and 6.
    The minimum strength in the tree is 6, which is the maximum possible stability.
    Example 3:

    Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0

    Output: -1

    Explanation:

    All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.
    

    Constraints:

    2 <= n <= 10^5
    1 <= edges.length <= 10^5
    edges[i] = [ui, vi, si, musti]
    0 <= ui, vi < n
    ui != vi
    1 <= si <= 10^5
    musti is either 0 or 1.
    0 <= k <= n
    
    python ./src/app/2025/July/3600.py
'''
import heapq
class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:

        parents, components, inf = [-1]*n, n, 10**9
        def find(x:int, nums:list[int]):
            parent = x
            while nums[parent] >= 0:
                parent=nums[parent]
            if parent!=x: nums[x]=parent
            return parent
        def union(a:int,b:int,nums:list[int]):
            pa,pb = find(a,nums), find(b,nums)
            if pa==pb: return False
            sa,sb = -nums[pa],-nums[pb]
            if sa>sb:
                nums[pb] = pa
                nums[pa] -= sb
            else: 
                nums[pa] = pb
                nums[pb] -= sa
            return True

        edgesPQ = [] 
        left, right = 0, inf
        for edge in edges:
            [u,v,s,must] = edge
            if must: 
                if not union(u,v,parents): return -1 #if cycle found in must-have edges
                components-=1
                right = min(right, s)
            else:
                heapq.heappush(edgesPQ, (-s,u,v))

        if components==1: return right
        elif edgesPQ: 
            right = min(
                right, 
                (-edgesPQ[0][0])*2 if k else -edgesPQ[0][0]
            )

        def canDo(stb:int):
            pq, uf = [[*edge] for edge in edgesPQ], [*parents]
            cnt, ops = components, k
            while len(pq) and cnt>1:
                s,u,v = heapq.heappop(pq)
                s *= -1

                ns = s*2 if ops else s
                if ns >= stb and union(u,v,uf): 
                    if s < stb: ops = max(0,ops-1)#if operation was used!
                    cnt-=1
                
            return cnt==1
        
        
        while left<right:
            stb = (left+right+1)//2
            if canDo(stb):
                left=stb
            else:
                right=stb-1
        return left if canDo(left) else -1
    

if __name__ == "__main__":
    testcases = []
    add = lambda n,edges,k: testcases.append([n,edges,k])
    # add(n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1)
    # add(n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2)
    # add(n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0)
    add(n=3, edges=[[0,1,84165,1],[0,2,96588,1],[1,2,24710,0]], k=2)

    sol = Solution()
    for [n,e,k] in testcases:
        print(f'n={n} edges={e} k={k} max-stability={sol.maxStability(n,e,k)}')