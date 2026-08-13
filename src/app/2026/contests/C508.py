import heapq

class Solution:
    '''
    3975. Filter Occupied Intervals

    You are given a 2D integer array occupiedIntervals, where occupiedIntervals[i] = [starti, endi] represents a time interval during which you are occupied. Each interval starts at starti and ends at endi, inclusive. These intervals may overlap.
    You are also given two integers freeStart and freeEnd, which define a free time interval from freeStart to freeEnd, inclusive.
    Your task is to merge all occupied intervals that overlap or touch, then remove all integer points in the free interval from the merged occupied intervals.
    Two intervals touch if the second interval starts immediately after the first one ends. For example, [1, 1] and [2, 2] touch and should be merged into [1, 2].
    Return the remaining occupied intervals in sorted order. The returned intervals must be non-overlapping and must contain the minimum number of intervals possible. If there are no remaining occupied points, return an empty list.

    Example 1:

    Input: occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11
    Output: [[2,6],[12,12],[14,16]]
    Explanation:
    After merging, the occupied intervals are [2, 8], [10, 12], and [14, 16].
    Excluding the free interval [7, 11] results in [2, 6], [12, 12], and [14, 16].

    Constraints:
    1 <= occupiedIntervals.length <= 5 * 10**4
    occupiedIntervals[i].length == 2
    1 <= starti <= endi <= 10**9
    1 <= freeStart <= freeEnd <= 10**9
    '''
    def filterOccupiedIntervals(self, ocpi: list[list[int]], fs: int, fe: int) -> list[list[int]]:
        ocpi.sort(key=lambda inv:(inv[0],inv[1]))
        res=[]
        for s,e in ocpi:
            ps,pe=res[-1] if res else [-2,-2]
            if s-1<=pe:
                res[-1][1]=max(pe,e)
            else: 
                res.append([s,e])
        ocpi=[]
        for s,e in res:
            if fs<=s<=e<=fe: 
                continue
            elif s<fs<=fe<e:
                ocpi.append([s,fs-1])
                ocpi.append([fe+1,e])
            elif fs<=s<=fe<e:
                ocpi.append([fe+1,e])
            elif s<fs<=e<=fe:
                ocpi.append([s,fs-1])
            elif e<fs or s>fe:
                ocpi.append([s,e])
        return ocpi
    '''
    3976. Maximum Subarray Sum After Multiplier

    You are given an integer array nums and a positive integer k.
    You must choose exactly one subarray of nums and perform exactly one of the following operations:
    Multiply each number in the chosen subarray by k.
    Divide each number in the chosen subarray by k.
    When dividing a positive number by k, use the floor value of the division result.
    When dividing a negative number by k, use the ceiling value of the division result.
    Return the maximum possible sum of a non-empty subarray in the resulting array.
    Note that the subarray chosen for the operation and the subarray chosen for the sum may be different.

    Example 1:
    Input: nums = [1,-2,3,4,-5], k = 2
    Output: 14
    Explanation:
    Multiply each number in the subarray [3, 4] by 2.
    This results in nums = [1, -2, 6, 8, -5].
    The subarray with the largest sum is [6, 8], so the output is 6 + 8 = 14.

    Constraints:
    1 <= nums.length <= 10**5
    -105 <= nums[i] <= 10**5
    1 <= k <= 10**5
    '''
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        op=[lambda x:x*k,lambda x: x//k if x>0 else (x+k-1)//k]
        inf=10**9; n=len(nums)
        res=-inf
        for i in range(2):
            dp1=[0]*n
            dp2=[0]*n
            dp3=[0]*n

            dp1[0]=nums[0]
            dp2[0]=op[i](nums[0])
            dp3[0]=-inf

            for j in range(1,n):
                curr=nums[j]
                val=op[i](curr)

                dp1[j]=max(curr,dp1[j-1]+curr)
                dp2[j]=max(val,dp1[j-1]+val,dp2[j-1]+val)
                dp3[j]=max(dp2[j-1]+curr,dp3[j-1]+curr,dp2[j])
            
            for j in range(n):
                res=max(res,dp1[j],dp2[j],dp3[j])
        return res
    '''
    3977. Minimum Time to Reach Target With Limited Power

    You are given a directed weighted graph with n nodes labeled from 0 to n - 1.
    The graph is represented by a 2D integer array edges, 
    where edges[i] = [ui, vi, ti] indicates a directed edge from node ui to node vi that takes ti seconds to traverse.
    You are also given an integer power representing the initial available power, and an integer array cost of length n,
    where cost[u] represents the power required to forward the signal from node u through any one of its outgoing edges.
    You are given two integers source and target.
    The signal starts at source at time 0 with power units of power and follows these rules:
    The signal may traverse a directed edge from node u only if the remaining power is at least cost[u].
    No power is consumed when the signal arrives at a node, unless it later leaves that node by traversing another edge.
    When the signal is forwarded from node u, the remaining power is decreased by cost[u] units.
    Traversing an edge edges[i] = [ui, vi, ti] increases the total time by ti seconds.
    Return an integer array answer of size 2, where:
    answer[0] is the minimum time required for the signal to reach node target.
    answer[1] is the maximum remaining power among all paths that achieve answer[0].
    If the signal cannot reach target, return [-1, -1].

    Constraints:
    1 <= n <= 1000
    0 <= edges.length <= 1000
    edges[i] = [ui, vi, ti]
    0 <= ui, vi <= n - 1
    1 <= ti <= 109
    1 <= power <= 1000
    cost.length == n
    1 <= cost[i] <= 2000
    0 <= source, target <= n - 1
    '''
    def minTimeMaxPower(self, n: int, edges: list[list[int]], power: int, cost: list[int], source: int, target: int) -> List[int]:
        graph=[[] for _ in range(n)]
        inf=10**18
        for u,v,t in edges:
            graph[u].append((v,t))
        
        res=[-1,-1]
        dist=[inf]*n
        q=[(0,source)]
        while q: 
            p,u=heapq.heappop(q)
            if p>power: 
                break
            if u==target: 
                res[1]=power-p
                break
            if p>dist[u]: continue
            dist[u]=p
            for v,_ in graph[u]:
                newcost=p+cost[v]
                if newcost<dist[v]:
                    dist[v]=newcost
                    heapq.heappush(q,(newcost,v))
        if res[1]<0: return [-1,-1]

        dist=[inf]*n
        q=[(0,source)]
        while q:
            p,u=heapq.heappop(q)
            if u==target: 
                res[0]=p
                break
            if p>dist[u]: continue
            dist[u]=p
            for v,t in graph[u]:
                newcost=p+t
                if newcost<dist[v]:
                    dist[v]=newcost
                    heapq.heappush(q,(newcost,v))
        return res

