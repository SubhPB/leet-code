from typing import List
class Solution:
    '''
    3784. Minimum Deletion Cost to Make All Characters Equal

    You are given a string s of length n and an integer array cost of the same length, where cost[i] is the cost to delete the ith character of s.
    You may delete any number of characters from s (possibly none), such that the resulting string is non-empty and consists of equal characters.
    Return an integer denoting the minimum total deletion cost required.

    Example 1:
    Input: s = "aabaac", cost = [1,2,3,4,1,10]
    Output: 11
    Explanation:
    Deleting the characters at indices 0, 1, 2, 3, 4 results in the string "c", which consists of equal characters, and the total cost is cost[0] + cost[1] + cost[2] + cost[3] + cost[4] = 1 + 2 + 3 + 4 + 1 = 11.

    Constraints:
    n == s.length == cost.length
    1 <= n <= 10^5
    1 <= cost[i] <= 10^9
    s consists of lowercase English letters.
    '''
    def minCost(self, s: str, cost: List[int]) -> int:
        freq={}; total=0
        for i,char in enumerate(s): 
            freq[char]=cost[i]+freq.get(char,0)
            total+=cost[i]
        res=total
        for char in freq: res=min(res,total-freq[char])
        return res
    '''
    3786. Total Sum of Interaction Cost in Tree Groups

    You are given an integer n and an undirected tree with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.
    You are also given an integer array group of length n, where group[i] denotes the group label assigned to node i.
    Two nodes u and v are considered part of the same group if group[u] == group[v].
    The interaction cost between u and v is defined as the number of edges on the unique path connecting them in the tree.
    Return an integer denoting the sum of interaction costs over all unordered pairs (u, v) with u != v such that group[u] == group[v].

    Example 1:
    Input: n = 3, edges = [[0,1],[1,2]], group = [1,1,1]
    Output: 4

    Explanation:
    All nodes belong to group 1. The interaction costs between the pairs of nodes are:
    Nodes (0, 1): 1
    Nodes (1, 2): 1
    Nodes (0, 2): 2
    Thus, the total interaction cost is 1 + 1 + 2 = 4.

    Constraints:
    1 <= n <= 10^5
    edges.length == n - 1
    edges[i] = [ui, vi]
    0 <= ui, vi <= n - 1
    group.length == n
    1 <= group[i] <= 20
    '''
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        res=0; graph=[[] for _ in range(n)]
        roots=[-1]*21
        for [u,v] in edges:
            graph[u].append(v)
            graph[v].append(u)
            roots[group[u]]=max(roots[group[u]], u)
            roots[group[v]]=max(roots[group[v]], v) 
        '''NEEDS MODIFICATION'''
        def dfs(u:int,p:int,d:int,src:List[int]):
            for v in graph[u]:
                if v!=p:
                    if group[v]==src[2]:
                        src[0]=2*src[0]+d*src[1]; src[1]+=1
                        dfs(v,u,1,src)
                    else:
                        dfs(v,u,d+1,src)
        for g in range(1,21):
            if roots[g]!=-1:
                src=[0,1,g]
                dfs(roots[g],-1,1,src)
                res+=src[0]
        return res