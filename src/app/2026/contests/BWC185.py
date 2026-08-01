class Solution:
    '''
    3964. Minimum Lights to Illuminate a Road

    You are given an integer array lights of length n, representing positions 0 through n - 1 on a road.
    For each position i:
    If lights[i] = v, where v > 0, there is a working bulb at position i that illuminates every position from max(0, i - v) to min(n - 1, i + v), inclusive.
    If lights[i] = 0, there is no working bulb at position i.
    A position is visible if it is illuminated by at least one working bulb.
    You may install additional bulbs at any positions. Each additional bulb installed at position j illuminates positions from max(0, j - 1) to min(n - 1, j + 1), inclusive.
    Return the minimum number of additional bulbs required to make every position on the road visible.
    
    Example 1:
    Input: lights = [0,0,0,0]
    Output: 2

    Explanation:
    One optimal placement is:
    Install an additional bulb at position 1, illuminating positions [0, 1, 2].
    Install an additional bulb at position 3, illuminating positions [2, 3].
    Therefore, the minimum number of additional bulbs required is 2.

    Constraints:
    1 <= n == lights.length <= 10**5
    0 <= lights[i] <= n
    '''
    def minLights(self, lights: list[int]) -> int:
        n=len(lights); res=0
        for i in range(n):
            if lights[i]>0:
                # increment bcz indexes are inclusive
                lights[i]+=1 
            if i>0:
                lights[i]=max(0,lights[i-1]-1,lights[i])
        for i in range(n-2,-1,-1):
            lights[i]=max(0,lights[i+1]-1,lights[i])
        for i in range(1,n+1):
            if lights[i-1]<=0:
                res+=1
                if i<n:
                    lights[i]=1 #any +ve value
                if i<n-1:
                    lights[i+1]=1 #any +ve value
        return res
    '''
    3965. Finish Time of Tasks I

    You are given an integer n representing the number of tasks in a project, numbered from 0 to n - 1. These tasks are connected as a tree rooted at task 0.
    This is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that task ui is the parent of task vi.
    You are also given an array baseTime of length n, where baseTime[i] represents the time to complete task i.
    The finish time of each task is calculated as follows:
    Leaf task: The finish time is baseTime[i].
    Non-leaf task:
    Let earliest be the minimum finish time among its children, and latest be the maximum finish time among its children.
    Let ownDuration be (latest - earliest) + baseTime[i].
    The finish time of task i is latest + ownDuration.
    Return the finish time of the root task 0.

    Example 1:
    Input: n = 3, edges = [[0,1],[1,2]], baseTime = [9,5,3]
    Output: 17

    Constraints:
    1 <= n <= 10**5
    edges.length = n - 1
    edges[i] == [ui, vi]
    0 <= ui, vi <= n - 1
    ui != vi
    1 <= baseTime[i] <= 10**5​​​​​​​
    The finish time of every task is guaranteed to be less than 2**53.
    '''
    def finishTime(self, n: int, edges: list[list[int]], baseTime: list[int]) -> int:
        if not n-1: return baseTime[0]
        parent=[0]*n
        graph=[[] for _ in range(n)]
        for u,v in edges:
            parent[v]=u
            graph[u].append(v)

        inf=10**18
        earliest=[inf]*n
        latest=[-inf]*n

        def finishTime(node:int):
            if not graph[node]: return baseTime[node]
            return 2*latest[node]-earliest[node]+baseTime[node]
        
        def dfs(node:int):
            u=parent[node]
            for v in graph[node]:
                dfs(v)
            if u!=node:
                earliest[u]=min(earliest[u],finishTime(node))
                latest[u]=max(latest[u],finishTime(node))
    
        dfs(0)

        return finishTime(0)

