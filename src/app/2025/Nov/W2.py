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
        n=len(nums);res=0;st=[]
        for num in nums:
            while st and st[-1]>num: st.pop()
            if not st or st[-1]<num: 
                st.append(num);res+=min(1,num)
        return res
    '''
    757. Set Intersection Size At Least Two

    You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.
    A containing set is an array nums where each interval from intervals has at least two integers in nums.
    For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
    Return the minimum possible size of a containing set.

    Example 1:

    Input: intervals = [[1,3],[3,7],[8,9]]
    Output: 5
    Explanation: let nums = [2, 3, 4, 8, 9].
    It can be shown that there cannot be any containing array of size 4.
    Constraints:

    1 <= intervals.length <= 3000
    intervals[i].length == 2
    0 <= starti < endi <= 10^8
    '''
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res=0;p1=-1;p2=-1;intervals.sort(key=lambda inv:(inv[1],-inv[0]))
        for [l,r] in intervals:
            if p2<l:
                p1,p2=r-1,r
                res+=2
            elif p1<l:
                res+=1
                p1,p2=p2,r
        return res
    '''
    3738. Longest Non-Decreasing Subarray After Replacing at Most One Element

    You are given an integer array nums.
    You are allowed to replace at most one element in the array with any other integer value of your choice.
    Return the length of the longest non-decreasing subarray that can be obtained after performing at most one replacement.
    An array is said to be non-decreasing if each element is greater than or equal to its previous one (if it exists).

    Example 1:
    Input: nums = [1,2,3,1,2]
    Output: 4
    Explanation:
    Replacing nums[3] = 1 with 3 gives the array [1, 2, 3, 3, 2].
    The longest non-decreasing subarray is [1, 2, 3, 3], which has a length of 4.

    Constraints:
    1 <= nums.length <= 10^5
    -109 <= nums[i] <= 10^9​​​​​​​
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        gamma=[];n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]: gamma.append(i)
        if not gamma: return n
        m=len(gamma)
        for i,z in enumerate(gamma):
            b=z-(gamma[i-1] if i else -1)
            f=(gamma[i+1] if i<m-1 else n)-z
            res=max(res,b,f)
            if 0<i<m-1 and nums[z-1]<=nums[z+1]:
                res=max(res,f+b-1)
        return res
    '''
    1018. Binary Prefix Divisible By 5
    You are given a binary array nums (0-indexed).
    We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
    For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
    Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

    Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
    '''
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x=0;n=len(nums)
        for i in range(n):
            x<<=1;x+=nums[i]
            nums[i]=not x%5
        return nums