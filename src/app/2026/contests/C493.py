from typing import List
class Solution:
    '''
    3871. Count Commas in Range II
    You are given an integer n.
    Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
    In standard formatting:
    A comma is inserted after every three digits from the right.
    Numbers with fewer than 4 digits contain no commas.

    Example 1:
    Input: n = 1002
    Output: 3
    Explanation:
    The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

    Constraints:
    1 <= n <= 10^15
    '''
    def countCommas(self, n: int) -> int:
        r=0; thl=[10**3,10**6,10**9,10**12,10**15]
        for t in thl:
            if n>=t: r+=n-(t-1)
        return r
    '''
    3872. Longest Arithmetic Sequence After Changing At Most One Element
    You are given an integer array nums.
    A subarray is arithmetic if the difference between consecutive elements in the subarray is constant.
    You can replace at most one element in nums with any integer. Then, you select an arithmetic subarray from nums.
    Return an integer denoting the maximum length of the arithmetic subarray you can select.

    Example 1:

    Input: nums = [9,7,5,10,1]
    Output: 5

    Explanation:
    Replace nums[3] = 10 with 3. The array becomes [9, 7, 5, 3, 1].
    Select the subarray [9, 7, 5, 3, 1], which is arithmetic because consecutive elements have a common difference of -2.
    Example 2:


    Constraints:
    4 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    '''
    def longestArithmetic(self, nums: List[int]) -> int:
        r=0;i=0;n=len(nums)
        while i<n:
            j=i+1
            while j<n-1 and 2*nums[j]==nums[j+1]+nums[j-1]:
                j+=1
            r=max(
                r,
                (j-i+1)+1
                +int(
                    (0<i-1<n-2 and nums[i-2]==3*nums[i]-2*nums[i+1])
                    or (j+2<n and nums[j+2]==3*nums[j]-2*nums[j-1])
                )
            )
            i=j
        return min(r,n)