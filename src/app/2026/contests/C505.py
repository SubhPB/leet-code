class Solution:
    '''
    3955. Valid Binary Strings With Cost Limit

    You are given two integers n and k.
    The cost of a binary string s is defined as the sum of all indices i (0-based) such that s[i] == '1'.
    A binary string is considered valid if:
    It does not contain two consecutive '1' characters.
    Its cost is less than or equal to k.
    Return a list of all valid binary strings of length n in any order.

    Example 1:
    Input: n = 3, k = 1
    Output: ["000","010","100"]
    Explanation:
    The binary strings of length 3 without consecutive '1' characters are:
    "000" : cost = 0
    "100" : cost = 0
    "010" : cost = 1
    "001" : cost = 2
    "101" : cost = 0 + 2 = 2
    Among these, the strings with cost less than or equal to k = 1 are "000", "010" and "100".
    Thus, the valid strings are ["000", "010", "100"].

    Constraints:
    1 <= n <= 12
    0 <= k <= n * (n - 1) / 2
    '''
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        pass        
    '''
    3956. Maximum Sum of M Non-Overlapping Subarrays I

    You are given an integer array nums of length n, and three integers m, l, and r.
    Your task is to select at least one and at most m non-overlapping subarrays from nums such that:
    Each selected subarray has a length between [l, r] (inclusive).
    The total sum of all selected subarrays is maximized.
    Return the maximum total sum you can achieve.
    
    Example 1:
    Input: nums = [4,1,-5,2], m = 2, l = 1, r = 3
    Output: 7
    Explanation:
    One optimal strategy is to:
    Select the subarray [4, 1] with sum 4 + 1 = 5 and the subarray [2] with sum 2. Both subarrays have length between [l, r].
    The total sum of these subarrays is 5 + 2 = 7, which is the maximum achievable sum with at most m = 2 subarrays.

    Constraints:
    1 <= n == nums.length <= 1000
    -10**9 <= nums[i] <= 10**9​​​​​​​
    1 <= m <= n
    1 <= l <= r <= n
    '''
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        # problème: complexité temporelle
        n=len(nums); mn=float('-inf')
        nums.append(0)
        for i in range(n):
            nums[i]+=nums[i-1]
            for j in range(max(0,i-r+1), i-l+2):
                mn=max(mn,nums[i]-nums[j-1])
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(1,m+1):
                for x in range(i+l-1,min(i+r,n)):
                    dp[i][j]=max(
                        dp[i][j],
                        nums[x]-nums[i-1]+dp[x+1][j-1],
                        dp[i+1][j]
                    )
        if not dp[0][m]:
            return mn
        return dp[0][m]