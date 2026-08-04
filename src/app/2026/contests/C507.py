from math import floor, log10
import heapq

class Solution:
    '''
    3969. Valid Subarrays With Matching Sum Digits I
    You are given an integer array nums and an integer digit x.
    A subarray nums[l..r] is considered valid if the sum of its elements satisfies both of the following conditions:
    The first digit of the sum is equal to x.
    The last digit of the sum is equal to x.
    Return the number of valid subarrays.

    Example 1:
    Input: nums = [1,100,1], x = 1
    Output: 4
    Explanation:
    The valid subarrays are:
    nums[0..0]: sum = 1
    nums[0..1]: sum = 1 + 100 = 101
    nums[1..2]: sum = 100 + 1 = 101
    nums[2..2]: sum = 1
    Thus, the answer is 4.

    Constraints:
    1 <= nums.length <= 1500
    1 <= nums[i] <= 109
    1 <= x <= 9
    '''
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        res=0;n=len(nums);nums.append(0)
        length= lambda val: floor(log10(val))+1
        for i in range(1,n):
            nums[i]+=nums[i-1]
        for l in range(1,n+1):
            for i in range(n-l+1):
                sm=nums[i+l-1]-nums[i-1]
                pw=length(sm)-1
                if x==sm//(10**pw)==sm%10:
                    res+=1
        return res
    '''
    3970. Shortest Path With At Most K Consecutive Identical Characters
    You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.
    You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.
    Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

    Example 1:
    Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
    Output: 3
    Explanation:
    The optimal valid path from node 0 to node 2 is as follows:
    Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
    The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

    Constraints:
    1 <= n == labels.length <= 5 * 10**4
    0 <= edges.length <= 5 * 10**4
    edges[i] == [ui, vi, wi]
    0 <= ui, vi <= n - 1
    ui != vi
    1 <= wi <= 10**4
    labels consists of lowercase English letters
    1 <= k <= 50
    '''
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        if not n-1: return 0
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
        inf=10**18; pq=[]
        dist=[[inf]*(k+1) for _ in range(n)]
        for v,w in graph[0]:
            c = 1 if labels[0]!=labels[v] else 2
            if c<=k: heapq.heappush(pq,(w,v,c))
        while pq:
            w,u,c=heapq.heappop(pq)
            # athere, c<=k always
            if u==n-1: return w
            elif w<dist[u][c]:
                dist[u][c]=w
                for v,d in graph[u]:
                    cnew= 1 if labels[u]!=labels[v] else c+1
                    dnew=d+w
                    if cnew>k: continue
                    for i in range(cnew+1):
                        if dist[v][i]<=dnew:
                            dnew=inf
                            break
                    if dist[v][cnew]>dnew:
                        heapq.heappush(pq,(dnew,v,cnew))
        return -1
