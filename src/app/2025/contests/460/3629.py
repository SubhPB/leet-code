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
from typing import List
from collections import deque, defaultdict

def is_prime(n: int) -> bool:
    if n < 2: return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0: return False
    return True

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)

        # Build div_map: p -> [i for which nums[i] % p == 0]
        div_map = defaultdict(list)
        for i, val in enumerate(nums):
            for p in range(2, int(val ** 0.5) + 1):
                if val % p == 0:
                    div_map[p].append(i)
                    if p != val // p:
                        div_map[val // p].append(i)
            if val > 1:
                div_map[val].append(i)  # val itself is always a divisor

        # BFS
        visited = [False] * n
        used_primes = set()
        q = deque([(0, 0)])  # (index, jumps)
        visited[0] = True

        while q:
            i, jumps = q.popleft()
            if i == n - 1:
                return jumps

            # Try adjacent moves
            for j in [i - 1, i + 1]:
                if 0 <= j < n and not visited[j]:
                    visited[j] = True
                    q.append((j, jumps + 1))

            # Try teleportation
            val = nums[i]
            if is_prime(val) and val not in used_primes:
                for j in div_map[val]:
                    if not visited[j]:
                        visited[j] = True
                        q.append((j, jumps + 1))
                used_primes.add(val)

        return -1  # should never happen per problem constraints
