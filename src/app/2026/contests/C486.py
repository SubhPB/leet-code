from typing import List
from collections import deque

class Solution:
    '''
    3819. Rotate Non Negative Elements
    You are given an integer array nums and an integer k.
    Rotate only the non-negative elements of the array to the left by k positions, in a cyclic manner.
    All negative elements must stay in their original positions and must not move.
    After rotation, place the non-negative elements back into the array in the new order, filling only the positions that originally contained non-negative values and skipping all negative positions.
    Return the resulting array.
    

    Example 1:
    Input: nums = [1,-2,3,-4], k = 3
    Output: [3,-2,1,-4]

    Explanation:​​​​​​​
    The non-negative elements, in order, are [1, 3].
    Left rotation with k = 3 results in:
    [1, 3] -> [3, 1] -> [1, 3] -> [3, 1]
    Placing them back into the non-negative indices results in [3, -2, 1, -4].

    Constraints:
    1 <= nums.length <= 10^5
    -105 <= nums[i] <= 10^5
    0 <= k <= 10^5
    '''
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        arr=[]; n=len(nums); res=list(nums)
        for i in range(n): 
            if nums[i]>-1: arr.append(i)
        for i,x in enumerate(arr):
            res[arr[i-k%len(arr)]]=nums[x]
        return res
    '''
    3820. Pythagorean Distance Nodes in a Tree

    You are given an integer n and an undirected tree with n nodes numbered from 0 to n - 1. The tree is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between ui and vi.
    You are also given three distinct target nodes x, y, and z.

    For any node u in the tree:
    Let dx be the distance from u to node x
    Let dy be the distance from u to node y
    Let dz be the distance from u to node z
    The node u is called special if the three distances form a Pythagorean Triplet.
    Return an integer denoting the number of special nodes in the tree.
    A Pythagorean triplet consists of three integers a, b, and c which, when sorted in ascending order, satisfy a2 + b2 = c2.
    The distance between two nodes in a tree is the number of edges on the unique path between them.

    Example 1:
    Input: n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3
    Output: 3

    Explanation:
    Node 0 has distances 1, 1, and 1. After sorting, the distances are 1, 1, and 1, which do not satisfy the Pythagorean condition.
    Node 1 has distances 0, 2, and 2. After sorting, the distances are 0, 2, and 2. Since 02 + 22 = 22, node 1 is special.
    Node 2 has distances 2, 0, and 2. After sorting, the distances are 0, 2, and 2. Since 02 + 22 = 22, node 2 is special.
    Node 3 has distances 2, 2, and 0. After sorting, the distances are 0, 2, and 2. This also satisfies the Pythagorean condition.
    Therefore, nodes 1, 2, and 3 are special, and the answer is 3.

    Constraints:
    4 <= n <= 10^5
    edges.length == n - 1
    edges[i] = [ui, vi]
    0 <= ui, vi, x, y, z <= n - 1
    x, y, and z are pairwise distinct.
    '''
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        G=[[] for _ in range(n)]; res=0
        for [u,v] in edges:
            G[u].append(v); G[v].append(u)
        def bfs(node:int):
            dist=[-1]*n; dist[node]=0; ls=deque([node])
            while ls:
                u=ls.popleft()
                for v in G[u]:
                    if dist[v]==-1:
                        dist[v]=dist[u]+1
                        ls.append(v)
            return dist
        [dx,dy,dz]=[bfs(node) for node in (x,y,z)]
        for i in range(n):
            [a,b,c]=sorted([dist[i] for dist in (dx,dy,dz)])
            res+=int(c*c==a*a+b*b)
        return res
    '''
    3821. Find Nth Smallest Integer With K One Bits
    You are given two positive integers n and k.
    Return an integer denoting the nth smallest positive integer that has exactly k ones in its binary representation. It is guaranteed that the answer is strictly less than 250.

    Example 1:
    Input: n = 4, k = 2
    Output: 9
    Explanation:
    The 4 smallest positive integers that have exactly k = 2 ones in their binary representations are:

    3 = 112
    5 = 1012
    6 = 1102
    9 = 10012
    
    Constraints:

    1 <= n <= 2^50
    1 <= k <= 50
    The answer is strictly less than 2^50
    '''
    def nthSmallest(self, n: int, k: int) -> int:
        pass