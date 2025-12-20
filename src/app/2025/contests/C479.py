from typing import List
class Solution:
    '''
    3771. Total Score of Dungeon Runs
    You are given a positive integer hp and two positive 1-indexed integer arrays damage and requirement.
    There is a dungeon with n trap rooms numbered from 1 to n. Entering room i reduces your health points by damage[i]. After that reduction, if your remaining health points are at least requirement[i], you earn 1 point for that room.
    Let score(j) be the number of points you get if you start with hp health points and enter the rooms j, j + 1, ..., n in this order.
    Return the integer score(1) + score(2) + ... + score(n), the sum of scores over all starting rooms.
    Note: You cannot skip rooms. You can finish your journey even if your health points become non-positive.

    

    Example 1:
    Input: hp = 11, damage = [3,6,7], requirement = [4,2,5]
    Output: 3

    Explanation:
    score(1) = 2, score(2) = 1, score(3) = 0. The total score is 2 + 1 + 0 = 3.

    As an example, score(1) = 2 because you get 2 points if you start from room 1.

    You start with 11 health points.
    Enter room 1. Your health points are now 11 - 3 = 8. You get 1 point because 8 >= 4.
    Enter room 2. Your health points are now 8 - 6 = 2. You get 1 point because 2 >= 2.

    Constraints:

    1 <= hp <= 10^9
    1 <= n == damage.length == requirement.length <= 10^5
    1 <= damage[i], requirement[i] <= 10^4
    '''
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n=len(damage);pf=[0]*(n+1); res=0
        for i in range(n): pf[i]+=damage[i]+pf[i-1]
        '''
        => hp-(d1+d2+...+dr) >= req[r]
        => hp-(pf[j]-pf[i-1]) >= req[r]
        => pf[i-1] >= req[r]+pf[r]-hp
        => score(r) = r-i+1
        '''
        def bs(target:int,r:int):
            l=-1
            while l<r:
                m=(l+r)//2
                if pf[m]>=target: r=m
                else: l=m+1
            return l
        for r in range(n):
            res+=r-bs(requirement[r]+pf[r]-hp,r)
        return res
    '''
    3772. Maximum Subgraph Score in a Tree
    You are given an undirected tree with n nodes, numbered from 0 to n - 1. It is represented by a 2D integer array edges​​​​​​​ of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
    You are also given an integer array good of length n, where good[i] is 1 if the ith node is good, and 0 if it is bad.
    Define the score of a subgraph as the number of good nodes minus the number of bad nodes in that subgraph.
    For each node i, find the maximum possible score among all connected subgraphs that contain node i.
    Return an array of n integers where the ith element is the maximum score for node i.
    A subgraph is a graph whose vertices and edges are subsets of the original graph.
    A connected subgraph is a subgraph in which every pair of its vertices is reachable from one another using only its edges.
    Example 1:
    Tree Example 1
    Input: n = 3, edges = [[0,1],[1,2]], good = [1,0,1]
    Output: [1,1,1]
    Explanation:
    Green nodes are good and red nodes are bad.
    For each node, the best connected subgraph containing it is the whole tree, which has 2 good nodes and 1 bad node, resulting in a score of 1.
    Other connected subgraphs containing a node may have the same score.

    Constraints:
    2 <= n <= 10^5
    edges.length == n - 1
    edges[i] = [ai, bi]
    0 <= ai, bi < n
    good.length == n
    0 <= good[i] <= 1
    The input is generated such that edges represents a valid tree.
    '''
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        G=[[] for _ in range(n)]
        for [u,v] in edges:
            G[u].append(v); G[v].append(u)
        res=[0]*n
        def dfs(node:int,parent:int):
            res[node] = 1 if good[node] else -1
            for neighbor in G[node]:
                if neighbor!=parent:
                    score=dfs(neighbor,node)
                    res[node]+=max(0,score)
            return res[node]
        dfs(0,-1)
        def dfs2(node:int,parent:int):
            if 0<=parent<n:
                res[node]=max(
                    res[node],
                    res[parent] + (-1 if res[node]<0 else 0)
                )
            for neighbor in G[node]:
                if neighbor!=parent: dfs2(neighbor, node)
        dfs2(0,-1)
        return res