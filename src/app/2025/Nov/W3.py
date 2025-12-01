from typing import List
class Solution:
    '''
    2435. Paths in Matrix Whose Sum Is Divisible by K

    You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.
    Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:

    Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
    Output: 2
    Explanation: There are two paths where the sum of the elements on the path is divisible by k.
    The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
    The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

    Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 5 * 10^4
    1 <= m * n <= 5 * 10^4
    0 <= grid[i][j] <= 100
    1 <= k <= 50
    '''
    def numberOfPaths(self, G: List[List[int]], k: int) -> int:
        m,n=len(G),len(G[0]);mod=10**9+7
        plus=lambda x,y: (x%mod+y%mod)%mod
        dp=[[[0]*k for _ in range(n)] for __ in range(m)]
        dp[m-1][n-1][(k-G[m-1][n-1]%k)%k]=1
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if (r,c)==(m-1,n-1): continue
                elif 0<=r<m and 0<=c<n:
                    for e in range(k):
                        en=(e+G[r][c])%k
                        if r!=m-1 and c!=n-1:
                            dp[r][c][e]=plus(dp[r+1][c][en],dp[r][c+1][en])
                        elif r==m-1:
                            dp[r][c][e]=dp[r][c+1][en]
                        else: 
                            dp[r][c][e]=dp[r+1][c][en]
        return dp[0][0][0]
    '''
    3751. Total Waviness of Numbers in Range I

    You are given two integers num1 and num2 representing an inclusive range [num1, num2].
    The waviness of a number is defined as the total count of its peaks and valleys:
    A digit is a peak if it is strictly greater than both of its immediate neighbors.
    A digit is a valley if it is strictly less than both of its immediate neighbors.
    The first and last digits of a number cannot be peaks or valleys.
    Any number with fewer than 3 digits has a waviness of 0.
    Return the total sum of waviness for all numbers in the range [num1, num2].

    Example 1:
    Input: num1 = 120, num2 = 130
    Output: 3

    Explanation:
    In the range [120, 130]:
    120: middle digit 2 is a peak, waviness = 1.
    121: middle digit 2 is a peak, waviness = 1.
    130: middle digit 3 is a peak, waviness = 1.
    All other numbers in the range have a waviness of 0.
    Thus, total waviness is 1 + 1 + 1 = 3.

    Constraints:
    1 <= num1 <= num2 <= 10^5
    '''
    def totalWaviness(self, num1: int, num2: int) -> int:
        E=0
        for num in range(num1,1+num2):
            num=str(num);n=len(num)
            for i in range(1,n-1):
                arr=sorted([num[i+j] for j in (-1,0,1)],key=lambda x:int(x))
                E+=int(arr[1]!=num[i])
        return E
    '''
    3752. Lexicographically Smallest Negated Permutation that Sums to Target
    You are given a positive integer n and an integer target.
    Return the lexicographically smallest array of integers of size n such that:

    The sum of its elements equals target.
    The absolute values of its elements form a permutation of size n.
    If no such array exists, return an empty array.

    A permutation of size n is a rearrangement of integers 1, 2, ..., n.

    Example 1:

    Input: n = 3, target = 0
    Output: [-3,1,2]

    Explanation:
    The arrays that sum to 0 and whose absolute values form a permutation of size 3 are:

    [-3, 1, 2]
    [-3, 2, 1]
    [-2, -1, 3]
    [-2, 3, -1]
    [-1, -2, 3]
    [-1, 3, -2]
    [1, -3, 2]
    [1, 2, -3]
    [2, -3, 1]
    [2, 1, -3]
    [3, -2, -1]
    [3, -1, -2]
    The lexicographically smallest one is [-3, 1, 2].

    Constraints:

    1 <= n <= 10^5
    -1010 <= target <= 10^10
    '''
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        '''
        Esum=target & abs(output[i]) ~ permutation 
        '''
        y=(n*(n+1))//2;nums=[x for x in range(n,0,-1)]
        if -y<=target<=y: 
            for i in range(n):
                if y==target: break
                yi=y-2*nums[i]
                if yi>=target: 
                    y=yi; nums[i]*=-1
            if y==target:
                nums.sort()
                return nums
        return []