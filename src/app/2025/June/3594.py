'''
3594. Minimum Time to Transport All Individuals

    You are given n individuals at a base camp who need to cross a river to reach a destination using a single boat. The boat can carry at most k people at a time. The trip is affected by environmental conditions that vary cyclically over m stages.

    Each stage j has a speed multiplier mul[j]:

    If mul[j] > 1, the trip slows down.
    If mul[j] < 1, the trip speeds up.
    Each individual i has a rowing strength represented by time[i], the time (in minutes) it takes them to cross alone in neutral conditions.

    Rules:

    A group g departing at stage j takes time equal to the maximum time[i] among its members, multiplied by mul[j] minutes to reach the destination.
    After the group crosses the river in time d, the stage advances by floor(d) % m steps.
    If individuals are left behind, one person must return with the boat. Let r be the index of the returning person, the return takes time[r] × mul[current_stage], defined as return_time, and the stage advances by floor(return_time) % m.
    Return the minimum total time required to transport all individuals. If it is not possible to transport all individuals to the destination, return -1.

    Example 1:

    Input: n = 1, k = 1, m = 2, time = [5], mul = [1.0,1.3]

    Output: 5.00000

    Explanation:

    Individual 0 departs from stage 0, so crossing time = 5 × 1.00 = 5.00 minutes.
    All team members are now at the destination. Thus, the total time taken is 5.00 minutes.
    Example 2:

    Input: n = 3, k = 2, m = 3, time = [2,5,8], mul = [1.0,1.5,0.75]

    Output: 14.50000

    Explanation:

    The optimal strategy is:

    Send individuals 0 and 2 from the base camp to the destination from stage 0. The crossing time is max(2, 8) × mul[0] = 8 × 1.00 = 8.00 minutes. The stage advances by floor(8.00) % 3 = 2, so the next stage is (0 + 2) % 3 = 2.
    Individual 0 returns alone from the destination to the base camp from stage 2. The return time is 2 × mul[2] = 2 × 0.75 = 1.50 minutes. The stage advances by floor(1.50) % 3 = 1, so the next stage is (2 + 1) % 3 = 0.
    Send individuals 0 and 1 from the base camp to the destination from stage 0. The crossing time is max(2, 5) × mul[0] = 5 × 1.00 = 5.00 minutes. The stage advances by floor(5.00) % 3 = 2, so the final stage is (0 + 2) % 3 = 2.
    All team members are now at the destination. The total time taken is 8.00 + 1.50 + 5.00 = 14.50 minutes.
    Example 3:

    Input: n = 2, k = 1, m = 2, time = [10,10], mul = [2.0,2.0]

    Output: -1.00000

    Explanation:

    Since the boat can only carry one person at a time, it is impossible to transport both individuals as one must always return. Thus, the answer is -1.00.
    

    Constraints:

    1 <= n == time.length <= 12
    1 <= k <= 5
    1 <= m <= 5
    1 <= time[i] <= 100
    m == mul.length
    0.5 <= mul[i] <= 2.0

    python ./src/app/2025/June/3594.py
'''
from itertools import combinations
from collections import deque, defaultdict
from typing import Deque
import heapq

class Solution:
    
    def minTime(self, n: int, k: int, m: int, time: list[int], mul: list[float]) -> float:

        def calcTimeTaken(maxTime:int, stage:int)->float:
            return float(maxTime*mul[stage])
        def calcNextStage(timeTaken:float, stage:int)->int:
            return int((
                stage + (timeTaken//1)%m
            )%m)
        
        if k==n==1: return calcTimeTaken(max(0, *time), 0) 
        elif k==1 and n>k: return -1.0
        
        # state E 12bits, stage E 3bits, zone E 1bit
        def encryptMask(state:int, stage:int, zone:int):
            return (state << 4) | (stage<<1) | zone
        def decryptMask(encryptedMask:int):
            mask, stage, zone = encryptedMask >> 4, (encryptedMask & 0b1111) >> 1, encryptedMask & 1
            return (mask, stage, zone)
        
        groupsCombinations:list[list[list[list[tuple[int, int]]]]] = [
            [
                [
                    [] for _ in range(2)
                ] for _ in range(k+1)
            ] for _ in range(2**n)
        ]# groupsCombinations[mask][capacity][zone] = list

        def possibleGroups(mask:int, capacity:int, zone:int):
            groups =  groupsCombinations[mask][capacity][zone]
            if not len(groups):
                folksInZone = []
                for sft in range(n):
                    if zone:
                        if mask & (1<<sft): folksInZone.append(sft)
                    else:
                        if not (mask & (1<<sft)): folksInZone.append(sft)
                        
                for group in combinations(folksInZone, capacity):
                    #nextMask is represent the next state of mask after traveling from one zone to another
                    nextMask, maxTime = mask, 0
                    for sft in group:
                        if zone: # Going from 'A' -> 'B', selected 1's would turn into 0's
                            nextMask = nextMask ^ (1<<sft)
                        else: # From 'B' -> 'A' selected 0's would turn into 1's
                            nextMask = nextMask | (1<<sft)
                        maxTime = max(maxTime, time[sft])
                    groups.append((nextMask, maxTime))
                groupsCombinations[mask][capacity][zone] = groups
            return groups

        # state: mask[i] if zero means node is at zone B else zone A
        initMask, initStage, initZone = 2**n-1, 0, 1, # (All nodes at zone 'A', 0-th stage, zone-A)

        initCost, target, inf = 0.0, 0, 1e9
        graph = defaultdict(dict[int])
        dq:Deque[tuple[int,int,int]] = deque([(initMask, initStage, initZone)])

        # Constructing graph
        while len(dq):
            mask, stage, zone = dq.popleft()

            currFullStateMask = encryptMask(mask, stage, zone)
            if currFullStateMask not in graph: graph[currFullStateMask] = {}

            population, nextZone = mask.bit_count() if zone else n - mask.bit_count(), (1+zone)%2
            maxCapacity = min(k, population)

            for capacity in range(1, 1+maxCapacity):
                for nextMask, maxTime in possibleGroups(mask, capacity, zone):
                    timeTaken = calcTimeTaken(maxTime, stage)
                    nextStage = calcNextStage(timeTaken, stage)

                    nextFullStateMask = encryptMask(nextMask, nextStage, nextZone)
                    
                    if nextFullStateMask in graph[currFullStateMask]: #if there's edge loop we will keep the minimum one!
                        graph[currFullStateMask][nextFullStateMask] = min(
                            graph[currFullStateMask][nextFullStateMask],
                            timeTaken
                        )
                    else:
                        graph[currFullStateMask][nextFullStateMask] = timeTaken
                        if nextMask != target:
                            dq.append(
                                (nextMask, nextStage, nextZone)
                            )
        
        #Dijkstra
        pq:list[tuple[int, int, int, int]] = [(initCost, initMask, initZone, initStage)]
        dp = [
            [
                [
                    inf for _ in range(2)
                ] for _ in range(m)
            ] for _ in range(2**n)
        ]#dp[mask][stage][zone] = minCost
        while len(pq):
            cost, mask, zone, stage = heapq.heappop(pq)
            if mask == target: return cost
            elif dp[mask][stage][zone] <= cost: continue

            dp[mask][stage][zone] = cost
            currFullStateMask = encryptMask(mask, stage, zone)

            for nextFullStateMask in graph[currFullStateMask]:
                nextMask, nextStage, nextZone = decryptMask(nextFullStateMask)
                nextCost = cost + graph[currFullStateMask][nextFullStateMask]
                heapq.heappush(pq, (nextCost, nextMask, nextZone, nextStage))

        return -1.0
                



                   
if __name__ == '__main__':
    testcases = []
    addTestCase = lambda n, k, m, time, mul: testcases.append([n,k,m,time,mul])

    addTestCase(n = 1, k = 1, m = 2, time = [5], mul = [1.0,1.3])
    addTestCase(n = 3, k = 2, m = 3, time = [2,5,8], mul = [1.0,1.5,0.75])
    addTestCase(n = 2, k = 1, m = 2, time = [10,10], mul = [2.0,2.0])
    addTestCase(n=2,k=3,m=4,time=[40,1],mul=[1.82,1.59,1.11,1.84])
    addTestCase(
        n = 9,
        k = 5,
        m = 4,
        time = [41,76,93,57,13,42,18,97,13],
        mul = [1.17,1.17,1.76,1.62],
    )

    sol= Solution()
    for [n,k,m,time,mul] in testcases:
        ans = sol.minTime(n,k,m,time,mul)

        print(f'n={n} k={k} m={m} time={time} mul={mul} minTime={ans}')
