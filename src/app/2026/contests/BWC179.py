'''#3883'''
dt=[[] for _ in range(51)]; mod=10**9+7
for i in range(5001):
    dgtsum=sum([int(x) for x in str(i)])
    if dgtsum<=50: dt[dgtsum].append(i)
    
def add(x:int,y:int):
    return (x%mod + y%mod)%mod
'''#3883'''

class Solution:
    '''
    3881. Direction Assignments with Exactly K Visible People
    You are given three integers n, pos, and k.
    There are n people standing in a line indexed from 0 to n - 1. Each person independently chooses a direction:
    'L': visible only to people on their right
    'R': visible only to people on their left
    A person at index pos sees others as follows:
    A person i < pos is visible if and only if they choose 'L'.
    A person i > pos is visible if and only if they choose 'R'.
    Return the number of possible direction assignments such that the person at index pos sees exactly k people.

    Since the answer may be large, return it modulo 109 + 7.
    
    Example 1:
    Input: n = 3, pos = 1, k = 0
    Output: 2
    Explanation:​​​​​​​
    Index 0 is to the left of pos = 1, and index 2 is to the right of pos = 1.
    To see k = 0 people, index 0 must choose 'R' and index 2 must choose 'L', keeping both invisible.
    The person at index 1 can choose 'L' or 'R' since it does not affect the count. Thus, the answer is 2.

    Constraints:
    1 <= n <= 10^5
    0 <= pos, k <= n - 1
    '''
    def exp(self, i:int,mod:int):
        r=1; b=i; p=mod-2
        while p>0:
            if p%2: r=(r*b)%mod
            b=(b*b)%mod
            p>>=1
        return r
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod=10**9+7; u=1; b=1; k=min(k,n-1-k)
        for i in range(1,1+k):
            u=(u*(n-i))%mod
            b=(b*i)%mod
        return (2*(self.exp(b,mod)*u)%mod)%mod
    '''
    3882. Minimum XOR Path in a Grid

    You are given a 2D integer array grid of size m * n.
    You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
    At each step, you may move either right or down.
    The cost of a path is defined as the bitwise XOR of all the values in the cells along that path,
    including the start and end cells.
    Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

    Example 1:
    Input: grid = [[1,2],[3,4]]
    Output: 6
    Explanation:
    There are two valid paths:
    (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
    (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
    The minimum XOR value among all valid paths is 6.


    Constraints:
    1 <= m == grid.length <= 1000
    1 <= n == grid[i].length <= 1000
    m * n <= 1000
    0 <= grid[i][j] <= 1023​
    '''
    def minCost(self, grid: list[list[int]]) -> int:
        m=len(grid); n=len(grid[0])
        dp=[[[-1]*1024 for _ in range(n)] for _ in range(m)]
        def dfs(i:int,j:int,x:int):
            if i>=m or j>=n: return 1023
            x^=grid[i][j]
            if (i,j)==(m-1,n-1): return x
            elif dp[i][j][x]==-1:
                right=dfs(i,j+1,x)
                down=dfs(i+1,j,x)
                dp[i][j][x]=min(right,down)
            return dp[i][j][x]
        return dfs(0,0,0)
    '''
    3883. Count Non Decreasing Arrays With Given Digit Sums

    You are given an integer array digitSum of length n.
    An array arr of length n is considered valid if:
        0 <= arr[i] <= 5000
        it is non-decreasing.
        the sum of the digits of arr[i] equals digitSum[i].
    Return an integer denoting the number of distinct valid arrays. Since the answer may be large, return it modulo 109 + 7.
    An array is said to be non-decreasing if each element is greater than or equal to the previous element, if it exists.

    Example 1:
    Input: digitSum = [25,1]
    Output: 6
    Explanation:

    Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997.
    The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000.
    Thus, the valid arrays are [799, 1000], [889, 1000], [898, 1000], [979, 1000], [988, 1000], and [997, 1000].
    Hence, the answer is 6.

    Constraints:
    1 <= digitSum.length <= 1000
    0 <= digitSum[i] <= 50
    '''
    def countArrays(self, digitSum: list[int]) -> int:
        dpv=dt[digitSum[-1]]; m=len(dpv); n=len(digitSum)
        Ev=[m-i for i in range(m)]
        if m: 
            for i in range(n-2,-1,-1):
                dpc=dt[digitSum[i]]
                mc=len(dpc); Ec=[0]*mc
                for j in range(mc-1,-1,-1):
                    #bs
                    l=0; r=m
                    while l<r:
                        mid=(l+r)//2
                        if dpv[mid]<dpc[j]: l=mid+1
                        else: r=mid
                    if l!=m:
                        Ec[j]=add((Ec[j+1] if j<mc-1 else 0), Ev[l])
                if not (Ec[0] if Ec else 0): return 0
                dpv=[*dpc]; Ev=[*Ec]; m=mc
            return Ev[0] 
        return 0