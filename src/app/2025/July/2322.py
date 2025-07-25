'''
2322. Minimum Score After Removals on a Tree

    There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

    You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

    Get the XOR of all the values of the nodes for each of the three components respectively.
    The difference between the largest XOR value and the smallest XOR value is the score of the pair.
    For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
    Return the minimum score of any possible pair of edge removals on the given tree.

    Example 1:

    Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
    Output: 9
    Explanation: The diagram above shows a way to make a pair of removals.
    - The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
    - The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
    - The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
    The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
    It can be shown that no other pair of removals will obtain a smaller score than 9.
    Example 2:

    Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
    Output: 0
    Explanation: The diagram above shows a way to make a pair of removals.
    - The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
    - The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
    - The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
    The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
    We cannot obtain a smaller score than 0.
    
    Constraints:

    n == nums.length
    3 <= n <= 1000
    1 <= nums[i] <= 10^8
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    edges represents a valid tree.
'''
from typing import List
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums); G = [[] for _ in range(n)]
        for [u,v] in edges: 
            G[u].append(v); G[v].append(u)


        LIFT = (n-1).bit_length(); dp = [
            [-1]*n for _ in range(LIFT)
        ] # dp[lift][node] = 2^lift-th parent of node

        XOR = [-1]*n; level = [-1]*n
        
        def dfs(u:int,parent:int):
            dp[0][u] = parent
            level[u]=level[parent]+1; XOR[u] = nums[u]
            for v in G[u]:
                if v != parent:
                    dfs(v,u)
                    XOR[u]^=XOR[v]
        dfs(0,-1)# calc node levels and xor of each subtree

        for lift in range(1,LIFT):
            for node in range(n):
                parent = dp[lift-1][node]
                dp[lift][node] = dp[lift-1][parent]
        
        def findParent(ith:int,node:int):
            i=0
            while ith and node!=-1:
                if ith&1: node = dp[i][node]
                ith>>=1
                i+=1
            return node

        def isMutualSubtree(u:int,v:int):
            diff = level[v]-level[u]
            if diff>0: v = findParent(diff,v)
            return v==u
        
        res = float('inf')
        for e1 in range(n-1):
            for e2 in range(e1+1,n-1):
                [_u1,v1] = sorted(edges[e1],key=lambda x:level[x])
                [_u2,v2] = sorted(edges[e2],key=lambda x:level[x])
                [v1,v2] = sorted([v1,v2],key=lambda x:level[x])

                if isMutualSubtree(v1,v2):
                    scores = sorted([XOR[0]^XOR[v1],XOR[v1]^XOR[v2],XOR[v2]])
                    res = min(
                        res, scores[-1]-scores[0]
                    )
                else:
                    scores = sorted([XOR[0]^XOR[v1]^XOR[v2],XOR[v1],XOR[v2]])
                    res = min(
                        res, scores[-1]-scores[0]
                    )
        return res