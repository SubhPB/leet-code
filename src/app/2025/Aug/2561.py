'''
    2561. Rearranging Fruits

    You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

    Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
    The cost of the swap is min(basket1[i],basket2[j]).
    Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

    Return the minimum cost to make both the baskets equal or -1 if impossible.

    

    Example 1:

    Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
    Output: 1
    Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
    Example 2:

    Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
    Output: -1
    Explanation: It can be shown that it is impossible to make both the baskets equal.
    

    Constraints:

    basket1.length == basket2.length
    1 <= basket1.length <= 10^5
    1 <= basket1[i],basket2[i] <= 10^9
'''

from typing import List
from collections import Counter
import heapq

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1 = Counter(basket1); c2 = Counter(basket2); res = 0
        imports = []; exports = []; leastCost = float('inf')
        for cost, countB2 in c2.items():
            countB1 = c1[cost]; totalCnt = countB1+countB2 
            if totalCnt&1: return -1
            diff = (countB1 - countB2)//2
            if diff>0: #need to export
                heapq.heappush(exports,(cost, diff))
            elif diff<0: # need to import
                heapq.heappush(imports,(-cost, -diff))
            leastCost = min(leastCost,cost)
        for cost, countB1 in c1.items(): #left-overs
            if c2[cost]>0: continue
            elif countB1&1: return -1
            diff = countB1//2
            if diff>0: heapq.heappush(exports,(cost,diff))
            leastCost = min(leastCost,cost)
        
        while imports:
            importCost, importCnt = heapq.heappop(imports); importCost = -importCost
            while importCnt>0:
                exportCost, exportCnt = heapq.heappop(exports)
                t = min(importCnt, exportCnt); tempCost = min(importCost, exportCost)
                res += min(tempCost*t, leastCost*2*t)
                importCnt -= exportCnt
                if importCnt<0: heapq.heappush(exports,(exportCost,-importCnt))

        return res
