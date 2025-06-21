'''
 * 3405. Count the Number of Arrays with K Matching Adjacent Elements

    You are given three integers n, m, k. A good array arr of size n is defined as follows:

    Each element in arr is in the inclusive range [1, m].
    Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
    Return the number of good arrays that can be formed.

    Since the answer may be very large, return it modulo 109 + 7.

    

    Example 1:

    Input: n = 3, m = 2, k = 1

    Output: 4

    Explanation:

    There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
    Hence, the answer is 4.
    Example 2:

    Input: n = 4, m = 2, k = 2

    Output: 6

    Explanation:

    The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
    Hence, the answer is 6.
    Example 3:

    Input: n = 5, m = 2, k = 0

    Output: 2

    Explanation:

    The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
    

    Constraints:

    1 <= n <= 10^5
    1 <= m <= 10^5
    0 <= k <= n - 1
    python ./src/app/2025/June/3405.py
'''

factorials = [1]*(1_00_001)
inv_factorials = [1]*(1_00_001)

class Solution:
    def __init__(self):
        self.M, self.MAX = 1_000_000_007, 1_00_000
        self.fact = factorials
        self.inv_fact = inv_factorials

    def MUL(x:int,y:int):
        return (x%1_000_000_007 * y%1_000_000_007)%1_000_000_007
    def binaryExp(base:int, pow:int):
        res=1
        while pow>0:
            if pow&1: res = Solution.MUL(res, base)
            base = Solution.MUL(base, base)
            pow //= 2
        return res
    
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        
        
        comb = lambda N,K: Solution.MUL(
            self.fact[N],
            Solution.MUL(self.inv_fact[K],self.inv_fact[N-K])
        )

        res, slots = 0, n-k
        res = Solution.MUL(
            comb(n-1, slots-1),
            Solution.MUL(
                m, Solution.binaryExp(m-1, slots-1)
            )
        )
        return res
    
for i in range(2,1_00_001):
    factorials[i] = Solution.MUL(factorials[i-1], i)
inv_factorials[1_00_000] = Solution.binaryExp(factorials[1_00_000],1_000_000_005)
for i in range(1_00_000-1, 0,-1):
    inv_factorials[i] = Solution.MUL(inv_factorials[i+1], i+1)