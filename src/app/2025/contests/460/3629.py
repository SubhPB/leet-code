'''
    3629. Minimum Jumps to Reach End via Prime Teleportation

    You are given an integer array nums of length n.

    You start at index 0, and your goal is to reach index n - 1.

    From any index i, you may perform one of the following operations:

    Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
    Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
    Return the minimum number of jumps required to reach index n - 1.

    

    Example 1:

    Input: nums = [1,2,4,6]

    Output: 2

    Explanation:

    One optimal sequence of jumps is:

    Start at index i = 0. Take an adjacent step to index 1.
    At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
    Thus, the answer is 2.

    Example 2:

    Input: nums = [2,3,4,7,9]

    Output: 2

    Explanation:

    One optimal sequence of jumps is:

    Start at index i = 0. Take an adjacent step to index i = 1.
    At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
    Thus, the answer is 2.

    Example 3:

    Input: nums = [4,6,5,8]

    Output: 3

    Explanation:

    Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.
    

    Constraints:

    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= 10^6
'''
from typing import List, Dict
from functools import cache
import heapq

def is_prime(n:int):
    if n<2: return False
    for d in range(2, int(n**(0.5))+1):
        if n%d==0: return False
    return True
def prime_multiple(n:int):
    if is_prime(n): return True
    if n>2:
        for d in range(2, int(n**(0.5))+1):
            if n%d == 0: return True
    return False
@cache
def prime_factors(n:int):
    factors=[]; i=2
    while i*i<n:
        if n%i == 0:
            factors.append(i)
            while n%i == 0: n//=i
        i+=1
    if n>1: factors.append(n)
    return factors

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums); G:Dict[int, List[int]] = {}
        for i in range(n):
            if is_prime(nums[i]): 
                if nums[i] not in G: G[nums[i]] = []
                G[nums[i]].append(i)
        pq = [(0, 0)] #(dist, node)[]
        push = lambda dist,node: heapq.heappush(pq, (dist, -node))

        dists = [float('inf')]*n
        while pq:
            d, u = heapq.heappop(pq); u = -u
            if u == n-1: return d
            elif d >= dists[u]: continue
            dists[u] = d

            if prime_multiple(nums[u]):
                factors = prime_factors(nums[u])
                for prime in factors:
                    if prime not in G: continue
                    for i in G[prime]:
                        if i == u: continue
                        elif dists[i] <= d: push(d, i)

            if d < dists[u+1]: push(d+1, u+1)
            if u>0 and dists[u-1] > d: push(d+1, u-1)

        return n-1