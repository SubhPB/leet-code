import math, heapq
class Solution:
    '''
    4001. Aggregate Two Time Series

    You are given two 2D integer arrays series1 and series2.
    Each element in both series is of the form [timestamp, value], where:
    timestamp is an integer representing the time.
    value is an integer representing the value at that timestamp.
    Each array is sorted in strictly increasing order of timestamp.
    For any timestamp not present in a series, its value is taken from the next available timestamp in the same series if one exists. Otherwise, its value is considered 0.
    The aggregated series is formed by summing the corresponding values from both series at every timestamp that appears in either series.
    Return the aggregated series as a 2D integer array of [timestamp, summedValue] pairs, sorted in strictly increasing order of timestamp.

    Example 1:
    Input: series1 = [[1,3],[4,1]], series2 = [[2,2],[5,2]]
    Output: [[1,5],[2,3],[4,3],[5,2]]

    Constraints:
    1 <= series1.length, series2.length <= 10**5
    series1[i].length == series2[i].length == 2
    1 <= series1[i][0], series2[i][0] <= 10**9
    1 <= series1[i][1], series2[i][1] <= 10**9
    Each series is sorted in strictly increasing order of timestamp.
    '''
    def aggregateTimeSeries(self, s1: list[list[int]], s2: list[list[int]]) -> list[list[int]]:
        val1=0;val2=0
        res=[]
        while s1 or s2:
            t=max(
                s[-1][0] for s in (s1,s2) if s
            )
            if s1 and s1[-1][0]==t: val1=s1.pop()[1]
            if s2 and s2[-1][0]==t: val2=s2.pop()[1]
            res.append([t,val1+val2])
        res.reverse()    
        return res
    '''
    4002. Count Valid Sequences

    You are given two positive integers n and k.
    A valid sequence is a sequence of k positive integers such that:
    The sum of all integers in the sequence is equal to n.
    The product of all integers in the sequence is even.
    Return the number of valid sequences. Since the answer may be very large, return it modulo 109​​​​​​​ + 7.
    Two sequences are considered different if they differ at any index. For example, [1, 1, 2] and [1, 2, 1] are considered different sequences.

    Example 1:
    Input: n = 5, k = 3
    Output: 3
    There are 3 sequences with an even product, thus the answer is 3.

    Constraints:
    1 <= n <= 5 * 10**5
    1 <= k <= n
    '''
    def countValidSequences(self, n: int, k: int) -> int:
        mod=10**9+7
        total=math.comb(n-1,k-1)%mod
        odd=0
        if (n-k)%2==0:
            odd=math.comb(
                (n-k)//2 + k-1, k-1
            )%mod
        if (n-k)%2==0:
            odd=math.comb(
                (n-k)//2 +k-1,k-1
            )
        return (total-odd)%mod
    '''
    4003. Minimum Cost Path with Alternating Directions III

    You are given two integers m and n representing the number of rows and columns of a grid. Your goal is to reach cell (m - 1, n - 1).
    You are also given a 2D integer array penalty.
    The cost to enter cell (i, j) is (i + 1) * (j + 1).
    You begin at cell (0, 0) and initially pay its entrance cost. Actions performed after entering (0, 0) are numbered starting from 1.
    On each action, you may move to an adjacent cell or wait in the current cell. A move follows the parity rule if:
    On an odd-numbered action, you move right or down.
    On an even-numbered action, you move left or up.

    The cost of an action is determined as follows:
    If you move according to the parity rule, pay only the entrance cost of the destination cell.
    If you move in a direction that violates the parity rule,
    pay the entrance cost of the destination cell plus penalty[i][j], where (i, j) is the cell you move from.
    If you wait in cell (i, j), pay penalty[i][j].
    After every move or wait, the action number increases by 1.
    Therefore, the required parity alternates after every action, regardless of whether a penalty was paid.
    Return the minimum total cost required to reach (m - 1, n - 1).

    Example 1:
    Input: m = 2, n = 2, penalty = [[5,3],[1,4]]
    Output: 8
    Explanation:
    The optimal path is:
    Start at cell (0, 0) with entry cost (0 + 1) * (0 + 1) = 1.
    Move 1: Move down to cell (1, 0) with entry cost (1 + 1) * (0 + 1) = 2.
    Move 2: Move right to cell (1, 1) with entry cost (1 + 1) * (1 + 1) = 4 and an extra cost of penalty[1][0] = 1 for violating the even parity rule.
    Thus, the total cost is 1 + 2 + 4 + 1 = 8.

    Constraints:
    1 <= m, n <= 10**5
    2 <= m * n <= 10**5
    penalty.length == m
    penalty[i].length == n
    0 <= penalty[i][j] <= 10**5
    '''
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        inf=10**18
        dist= [
            [[inf]*n for _ in range(m)] for t in range(2)
        ]
        pq=[]
        base=(1,1,0,0)
        pq.append(base)
        while pq:
            cost,time,i,j=heapq.heappop(pq)
            if (i,j)==(m-1,n-1):
                return cost
            
            if cost>=dist[time][i][j]:
                continue
            dist[time][i][j]=cost

            if time%2: #odd_action
                ni,nj=i,j+1 #right
                if nj<n:
                    new_cost=cost+(ni+1)*(nj+1)
                    if new_cost<dist[(time+1)%2][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,(time+1)%2,ni,nj)
                        )
                ni,nj=i+1,j #down
                if ni<m:
                    new_cost=cost+(ni+1)*(nj+1)
                    if new_cost<dist[(time+1)%2][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,(time+1)%2,ni,nj)
                        )

                # going_against_the_parity_rule -> opposite_dir
                ni,nj=i,j-1 #left
                if nj>=0:
                    new_cost=cost+(ni+1)*(nj+1)+penalty[i][j]
                    if new_cost<dist[time][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,time,ni,nj)
                        )
                ni,nj=i-1,j #up
                if ni>=0:
                    new_cost=cost+(ni+1)*(nj+1)+penalty[i][j]
                    if new_cost<dist[time][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,time,ni,nj)
                        )
            else: #even_action
                ni,nj=i,j-1 #left
                if nj>=0:
                    new_cost=cost+(ni+1)*(nj+1)
                    if new_cost<dist[(time+1)%2][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,(time+1)%2,ni,nj)
                        )
                ni,nj=i-1,j #up
                if ni>=0:
                    new_cost=cost+(ni+1)*(nj+1)
                    if new_cost<dist[(time+1)%2][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,(time+1)%2,ni,nj)
                        )

                # going_against_the_parity_rule -> opposite_dir
                ni,nj=i,j+1 #right
                if nj<n:
                    new_cost=cost+(ni+1)*(nj+1)+penalty[i][j]
                    if new_cost<dist[time][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,time,ni,nj)
                        )
                ni,nj=i+1,j #down
                if ni<m:
                    new_cost=cost+(ni+1)*(nj+1)+penalty[i][j]
                    if new_cost<dist[time][ni][nj]:
                        heapq.heappush(
                            pq, (new_cost,time,ni,nj)
                        )
        return -1 #not_possible