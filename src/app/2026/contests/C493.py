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
        r=0; z=[-1]; n=len(nums); i=2
        while i<n:
            if nums[i-1]*2 != nums[i]+nums[i-2]:
                z.append(i-1); i+=1
            i+=1
        if z[-1]!=n-1: z.append(n-1)
        for i in range(1,len(z)):
            lx=z[i-1]; ri=z[i]
            r=max(
                r,
                ri-lx+1
                +int(
                    (lx>1 and 3*nums[lx-1]-2*nums[lx-2] == nums[lx+1])
                    or (ri<n-2 and 3*nums[ri]-2*nums[ri-1] == nums[ri+2])
                )
            )
        return min(n,r)