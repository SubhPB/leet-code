from typing import List
class Solution:
    '''
        1611. Minimum One Bit Operations to Make Integers Zero
        Given an integer n, you must transform it into 0 using the following operations any number of times:
        Change the rightmost (0th) bit in the binary representation of n.
        Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
        Return the minimum number of operations to transform n into 0.

        Example 1:

        Input: n = 3
        Output: 2
        Explanation: The binary representation of 3 is "11".
        "11" -> "01" with the 2nd operation since the 0th bit is 1.
        "01" -> "00" with the 1st operation.
    '''
    def minimumOneBitOperations(self, n: int) -> int:
        pass
    '''
    474. Ones and Zeroes
    You are given an array of binary strings strs and two integers m and n.
    Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
    A set x is a subset of a set y if all elements of x are also elements of y.

    Example 1:

    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
    Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
    {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

    Constraints:
    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of digits '0' and '1'.
    1 <= m, n <= 100
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            x=s.count('1');y=len(s)-x
            for i in range(m,y-1,-1):
                for j in range(n,x-1,-1):
                    dp[i][j]=max(
                        dp[i][j],
                        1+dp[i-y][j-x]
                    )
        return dp[m][n]
    '''
    3542. Minimum Operations to Convert All Elements to Zero
    You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.
    In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.
    Return the minimum number of operations required to make all elements in the array 0.

    Example 1:
    Input: nums = [0,2]
    Output: 1
    Explanation:
    Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
    Thus, the minimum number of operations required is 1.
    Example 2:
    Input: nums = [3,1,2,1]
    Output: 3

    Explanation:

    Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
    Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
    Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
    Thus, the minimum number of operations required is 3.

    Constraints:
    1 <= n == nums.length <= 10^5
    0 <= nums[i] <= 10^5
    '''
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums);freq={};res=0
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]]=[]
            freq[nums[i]].append(i)
        for idxs in freq.values():
            m=len(idxs); num=nums[idxs[0]]
            if not num:continue
            res+=1
            for i in range(m-1):
                for j in range(idxs[i],idxs[i+1]):
                    if nums[j]<num:
                        res+=1;i+=1
                        break
        return res