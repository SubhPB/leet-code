perm=[1]*14 #3910 @cache
for i in range(1,14):
    perm[i]=i*perm[i-1]

class Solution:
    '''
    3909. Compare Sums of Bitonic Parts
    You are given a bitonic array nums of length n.
    Split the array into two parts:
    Ascending part: from index 0 to the peak element (inclusive).
    Descending part: from the peak element to index n - 1 (inclusive).
    The peak element belongs to both parts.
    Return:
    0 if the sum of the ascending part is greater.
    1 if the sum of the descending part is greater.
    -1 if both sums are equal.

    Example 1:
    Input: nums = [1,3,2,1]
    Output: 1

    Constraints:
    3 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    nums is a bitonic array.
    '''
    def compareBitonicSums(self, nums: list[int]) -> int:
        s=nums[0]; n=len(nums); p=s
        for i in range(1,n):
            p=max(p,nums[i])
            s+=nums[i]*[-1,1][int(nums[i]>nums[i-1])]
        s-=p
        if s!=0:
            return 0 if s>0 else 1
        return -1
    '''
    3910. Count Connected Subgraphs with Even Node Sum

    You are given an undirected graph with n nodes labeled from 0 to n - 1. Node i has a value of nums[i], which is either 0 or 1.
    The edges of the graph are given by a 2D array edges where edges[i] = [ui, vi] represents an edge between node ui and node vi.
    For a non-empty subset s of nodes in the graph, we consider the induced subgraph of s generated as follows
    We keep only the nodes in s.
    We keep only the edges whose two endpoints are both in s.
    Return an integer representing the number of non-empty subsets s of nodes in the graph such that:
    The induced subgraph of s is connected.
    The sum of node values in s is even.

    Example 1:
    Input: nums = [1,0,1], edges = [[0,1],[1,2]]
    Output: 2

    Constraints:
    1 <= n == nums.length <= 13
    nums[i] is 0 or 1.
    0 <= edges.length <= n * (n - 1) / 2
    edges[i] = [ui, vi]
    0 <= ui < vi < n
    All edges are distinct.
    '''
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n=len(nums); parent=[-1]*n
        def find(x:int):
            p=x
            while parent[p]>-1:
                p=parent[p]
            if p!=x: parent[x]=p
            return p
        def union(x:int,y:int):
            px=find(x); py=find(y)
            if px!=py:
                if parent[px]<parent[py]:
                    parent[px]+=parent[py]
                    parent[py]=px
                else:
                    parent[py]+=parent[px]
                    parent[px]=py
                return True
            return False
        for [u,v] in edges: union(u,v)
        C = lambda a,b: int(perm[a]/(perm[b]*perm[a-b]))
        res=0
        for p in range(n):
            if parent[p]>-1: continue
            l=-parent[p]
            x=sum([
                int(p in [i,parent[i]] and nums[i])
                for i in range(n)
            ])
            y=l-x
            k=sum([C(y,i) for i in range(y+1)])
            u=sum([C(x,i) for i in range(0,x+1,2)])
            res+=k*u-1
        return res
    '''
    3911. K-th Smallest Remaining Even Integer in Subarray Queries
    You are given an integer array nums where nums is strictly increasing.
    You are also given a 2D integer array queries, where queries[i] = [li, ri, ki].
    For each query [li, ri, ki]:
    Consider the subarray nums[li..ri]
    From the infinite sequence of all positive even integers: 2, 4, 6, 8, 10, 12, 14, ...
    Remove all elements that appear in the subarray nums[li..ri].
    Find the kith smallest integer remaining in the sequence after the removals.
    Return an integer array ans, where ans[i] is the result for the ith query.
    
    Example 1:
    Input: nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]
    Output: [2,6,6]

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**9
    nums is strictly increasing
    1 <= queries.length <= 10**5
    queries[i] = [li, ri, ki]
    0 <= li <= ri < nums.length
    1 <= ki <= 10**9​​​​​​​
    '''
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        '''
        m=len(queries)
        Δp'= 2*ki+ 2*count(e W e<=2*ki)
        Δp = Δp' + 2*count(e W 2*ki<e<=Δp')
        res[i]=Δp
        '''
        pass