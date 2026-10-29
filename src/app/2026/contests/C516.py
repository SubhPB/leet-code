class Solution:
    '''
    4031. Find All Numbers Disappeared in an Array II

    You are given an integer array nums and two integers lower and upper.
    A missing integer is an integer in the inclusive range [lower, upper] that does not appear in nums.
    Return a 2D integer array where each element is of the form [start, end], representing a contiguous range of missing integers.
    Return the ranges in increasing order. If there are no missing integers, return an empty array.
    Note: Consecutive missing integers should be grouped into a single range.
    
    Example 1:

    Input: nums = [3,9,7], lower = 1, upper = 12
    Output: [[1,2],[4,6],[8,8],[10,12]]


    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**5
    1 <= lower <= upper <= 10**5
    '''
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.append(0)
        nums.sort()
        if nums[-1]<upper:
            nums.append(upper+1)
        n=len(nums)
        res=[]
        for i in range(1,n):
            start=max(nums[i-1]+1,lower)
            end=min(nums[i]-1,upper)
            if lower<=start<=end<=upper:
                res.append([start,end])

        return res
    '''
    4032. Longest Subarray With at Most K Distinct Prime Factors

    You are given an integer array nums consisting of positive integers and an integer k.
    The prime factor set of a subarray is the union of the distinct prime factors of all its elements.
    Return the length of the longest subarray whose prime factor set contains at most k distinct prime factors. If no such subarray exists, return 0.

    Example 1:
    Input: nums = [7,6,10,12,11], k = 3

    Output: 3
    Explanation:
    Consider the subarray [6, 10, 12]:
    The distinct prime factors of 6 are {2, 3}.
    The distinct prime factors of 10 are {2, 5}.
    The distinct prime factors of 12 are {2, 3}.
    The union of these sets is {2, 3, 5}, which contains 3 distinct prime factors.
    No longer subarray satisfies the condition. Therefore, the answer is 3.

    Constraints:
    1 <= nums.length <= 10**5
    2 <= nums[i] <= 10**5
    1 <= k <= 10**4
    '''
    def longestSubarray(self, nums: list[int], k: int) -> int:
        pass
    '''
    4033. Valid K-Unique Subarrays I

    You are given an integer array nums and an integer k.
    You are also given a 2D integer array queries, where queries[i] = [li, ri] represents the subarray nums[li..ri].
    For each query, the subarray nums[li..ri] is considered valid if:
    It contains exactly k distinct numbers, and
    The frequency of every number in the subarray is even.
    Return a boolean array ans, where ans[i] is true if nums[li..ri] is valid, and false otherwise.

    Example 1:
    Input: nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]
    Output: [false,true,false]

    Constraints:
    2 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**5
    1 <= k <= n
    1 <= queries.length <= 10**5
    queries[i] == [li, ri]
    0 <= li < ri <= n - 1
    '''
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        pass