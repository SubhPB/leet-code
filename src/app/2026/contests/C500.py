# ----#3918----
def isPrime(x:int):
    if x in [2,3,5,7]:
        return True
    if x==1 or 0 in [x%2,x%3,x%5]: 
        return False
    y=6
    while y*y<=x:
        if not x%(y+1):
            return False
        elif not x%(y+5):
            return False
        y+=6
    return True
# ----#3918----
cache=[0]*1001
for x in range(1,1001):
    if isPrime(x): 
        cache[x]=x
    cache[x]+=cache[x-1]

class Solution:
    '''
    3918. Sum of Primes Between Number and Its Reverse

    You are given an integer n.
    Let r be the integer formed by reversing the digits of n.
    Return the sum of all prime numbers between min(n, r) and max(n, r), inclusive.
    
    Example 1:
    Input: n = 13
    Output: 132
    Explanation:
    The reverse of 13 is 31. Thus, the range is [13, 31].
    The prime numbers in this range are 13, 17, 19, 23, 29, and 31.
    The sum of these prime numbers is 13 + 17 + 19 + 23 + 29 + 31 = 132.

    Constraints:
    1 <= n <= 1000
    '''
    def sumOfPrimesInRange(self, n: int) -> int:
        r=int(''.join([*str(n)][::-1]))
        return cache[max(n,r)]-cache[min(n,r)-1]
    '''
    3919. Minimum Cost to Move Between Indices

    You are given an integer array nums where nums is strictly increasing.
    For each index x, let closest(x) be the adjacent index y such that abs(nums[x] - nums[y]) is minimized. If both adjacent indices exist and give the same difference, choose the smaller index.
    From any index x, you can move in two ways:
    To any index y with cost abs(nums[x] - nums[y]), or
    To closest(x) with cost 1.
    You are also given a 2D integer array queries, where each queries[i] = [li, ri].
    For each query, calculate the minimum total cost to move from index li to index ri.
    Return an integer array ans, where ans[i] is the answer for the ith query.
    The absolute difference between two values x and y is defined as abs(x - y).

    Example 1:
    Input: nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]
    Output: [6,2,5]
    Explanation:​​​​​​​​​​​​​​​​​​​​
    The closest indices are [1, 0, 1] respectively.
    For [0, 2], the path 0 → 1 → 2 uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost |-2 - 3| = 5, giving total 1 + 5 = 6.
    For [2, 0], the path 2 → 1 → 0 uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2.
    For [1, 2], the direct move from index 1 to index 2 has cost |-2 - 3| = 5, which is optimal.
    Thus, ans = [6, 2, 5].
    
    Constraints:
    2 <= nums.length <= 10**5
    -10**9 <= nums[i] <= 10**9
    nums is strictly increasing
    1 <= queries.length <= 10**5
    queries[i] = [li, ri]​​​​​​​
    0 <= li, ri < nums.length
    '''
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n=len(nums); m=len(queries); cost=[0]*n
        cost[1]=1
        for i in range(2,n):
            cost[i]=cost[i-1]
            if abs(nums[i-1]-nums[i-2])>abs(nums[i-1]-nums[i]):
                cost[i]+=1
            else:
                cost[i]+=abs(nums[i-1]-nums[i])
        for i in range(m):
            [l,r]=queries[i]
            if l<r: queries[i]=cost[r]-cost[l-1]
        cost[n-1]=0; cost[n-2]=1
        for i in range(n-3,-1,-1):
            cost[i]=cost[i+1]
            if abs(nums[i+1]-nums[i+2])>abs(nums[i+1]-nums[i]):
                cost[i]+=1
            else:
                cost[i]+=abs(nums[i+1]-nums[i])
        for i in range(m):
            if isinstance(queries[i],list):
                [l,r]=queries[i]
                queries[i]=cost[l]-cost[r]
        return queries