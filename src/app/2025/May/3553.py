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
        n = len(edges)+1

        parent = [-1]*n # parent of ith node
        weight = [-1]*n # weight btw ith node to its parent
        depth = [0]*n # At what level does ith node exist?

        '''
        Need to sort the edges to construct a valid graph
        '''
        for u,v,w in edges:
            parent[v] = u
            weight[v] = w
            depth[v] = depth[u]+1

        res = []
        for a,b,c in queries:
            depths = [depth[i] for i in [a,b,c]]
            depths.sort()
            top = depths[0]

            if depths.count(top) > 1: 
                top -= 1

            cost_sum=0
            nodes = [a,b,c]
            nodes.sort(key= lambda x: depth[x])#sort acc node which is more close to the top

            for i in range(3):
                node=nodes[i]
                lvl = depth[node]
                while lvl != top:
                    cost_sum += weight[node]
                    node = parent[node]
                    lvl = depth[node]
                    if i>0 and node == nodes[i-1]:
                        break
            res.append(cost_sum)
        return res

    def minimumWeightTopSubmission(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges)+1# cnt of nodes in graph

        graph = [[] for _ in range(n)]
        for u, v, w in edges:#undirected-tree / adjacency-list
            graph[u].append((v,w))
            graph[v].append((u,w))

        '''
        At most a node can be at height of (n-1) as an extreme case, means deepest node has at most n-1 distance from root.

        BINARY LIFTING:-
            BinaryLifting is a technique used to move up the tree quickly using powers of 2.
            e.g. if node is deep and say at depth 19 you want to jump-up to its 19th ancestor
                then you can climb in powers of 2
                Go up 2⁴ = 16 levels (3 left)
                Then go up 2¹ = 2 levels (1 left)
                Then go up 2⁰ = 1 level (0 left)
            Suppose n - 1 = 13 what are max power of 2 would we need to get close to 13?
                2³ = 8, but how 13 can be written as 2³ + 2² + 2⁰
                which makes max_binary_lift = bit-length-of-13 or we can either choose ceil(log2(n))
        '''    
        #max-depth for binary lifting (ceil(log2(n))) in the worst case
        mx_binary_lift = (n-1).bit_length()

        ancestor = [ #BinaryLifting table: ancestor[pow][node] = 2^pow-th ancestor of 'node'
            [-1]*n for _ in range(mx_binary_lift)
        ]

        #depth of ith node from the root
        depth = [0]*n

        dist_from_root = [0]*n#ith node's distance from root

        #Step 2: DFS to set parent, depth, prefix-sum weight arrays
        def dfs(node:int, parent:int): 
            ancestor[0][node] = parent#2^0=1; closest parent
            for neighbor, weight in graph[node]:
                if neighbor == parent: 
                    #according to argument we're said to treat node as child of parent
                    continue
                depth[neighbor] = depth[node]+1
                dist_from_root[neighbor] = dist_from_root[node] + weight
                dfs(
                    neighbor,
                    node
                )
        dfs(0, -1)

        #Step 3: Binary lifting table preprocessing
        for pow in range(1, mx_binary_lift):
            for node in range(n):
                prev_ancestor = ancestor[pow-1][node]
                if prev_ancestor != -1:
                    ancestor[pow][node] = ancestor[pow-1][prev_ancestor]
        
        #Step 4: LCA computation using binary lifting
        '''
        LCA: LowestCommonAncestor
        Given u and v, lca will find the lowest common ancestor among them!
        '''
        def get_lca(u:int, v:int) -> int:
            if depth[u] < depth[v]:
                #ensure 'u' is deeper node
                u, v = v, u 

            diff = depth[u] - depth[v]
            for k in range(mx_binary_lift): # try to bring same depth as of 'v'
                if (diff >> k) & 1:
                    '''
                    Suppose depth[u] = 11, depth[v] = 6
                    e.g. diff = 0b101 = 5
                        (0b101 >> 0) & 1 = 1 -> u = ancestor[0][u] [Has moved to level 10, 'u' has updated]
                        (0b101 >> 1) & 1 = 0 
                        (0b101 >> 2) & 1 = 0 -> new_u = ancestor[2][new_u], moved up to 10 - 4 = 6th level
                    '''
                    u = ancestor[k][u]

                if u == v:#If u lied under the v
                    return u
                
                #Lift both u and v together until their ancestors match
                for k in range(mx_binary_lift-1, -1, -1):
                    if ancestor[k][u] != ancestor[k][v]:
                        u = ancestor[k][u]
                        v = ancestor[k][v]
                return ancestor[0][u]
            
        #Step 5: distance btw any two nodes via prefix sums
        def get_dist(u:int, v:int)->int:
            lca = get_lca(u,v)
            return dist_from_root[u] + dist_from_root[v] - 2*dist_from_root[lca]
        
        res = [0]*len(queries)
        for (qi, [src1, src2, dest])  in enumerate(queries):
            d1 = get_dist(src1, src2)
            d2 = get_dist(src1, dest)
            d3 = get_dist(src2, dest)
            res[qi] = int(
                (d1+d2+d3) // 2
            )
           
        return res

        
