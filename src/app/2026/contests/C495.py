from typing import List
class Solution:
    '''
    3886. Sum of Sortable Integers

    You are given an integer array nums of length n.
    An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:
    Partition nums into consecutive subarrays of length k.
    Cyclically rotate each subarray independently any number of times to the left or to the right.
    Return an integer denoting the sum of all possible sortable integers k.

    Example 1:
    Input: nums = [3,1,2]
    Output: 3
    Explanation:​​​​​​​

    For n = 3, possible divisors are 1 and 3.
    For k = 1: each subarray has one element. No rotation can sort the array.
    For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
    Only k = 3 is sortable. Hence, the answer is 3.

    Constraints:
    1 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**5
    '''
    def λ(self, nums:int, length:int):
        n=len(nums); prv=0
        for i in range(0,n,length):
            curr=nums[i]; brk=nums[i]<nums[i+length-1]
            if prv>curr: return False
            for j in range(i+1,i+length):
                if nums[j]<nums[j-1]:
                    if brk: return False
                    brk=True
                curr=max(curr,nums[j])
                if prv>nums[j]: return False
            prv=curr
        return True
    def sortableIntegers(self, nums: list[int]) -> int:
        res=0; n=len(nums)
        for l in range(n):
            if n%(l+1): continue
            if self.λ(nums,l+1):
                res+=l+1
        return res
    '''
    3887. Incremental Even-Weighted Cycle Queries
    You are given a positive integer n.
    There is an undirected graph with n nodes labeled from 0 to n - 1. Initially, the graph has no edges.
    You are also given a 2D integer array edges, where edges[i] = [ui, vi, wi] represents an edge between nodes ui and vi with weight wi. The weight wi is either 0 or 1.
    Process the edges in edges in the given order. For each edge, add it to the graph only if, after adding it, the sum of the weights of the edges in every cycle in the resulting graph is even.
    Return an integer denoting the number of edges that are successfully added to the graph.

    Example 1:
    Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,1]]
    Output: 2
    Explanation:
    [0, 1, 1]: We add the edge between vertex 0 and vertex 1 with weight 1.
    [1, 2, 1]: We add the edge between vertex 1 and vertex 2 with weight 1.
    [0, 2, 1]: The edge between vertex 0 and vertex 2 (the dashed edge in the diagram),
    is not added because the cycle 0 - 1 - 2 - 0 has total edge weight 1 + 1 + 1 = 3, which is an odd number.
    
    Constraints:
    3 <= n <= 5 * 10**4
    1 <= edges.length <= 5 * 10**4
    edges[i] = [ui, vi, wi]
    0 <= ui < vi < n
    All edges are distinct.
    wi = 0 or wi = 1
    '''
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        # incomplete...
        pass