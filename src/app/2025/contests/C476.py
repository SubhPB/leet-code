from typing import List
class Solution:
    '''
        3746. Minimum String Length After Balanced Removals
        You are given a string s consisting only of the characters 'a' and 'b'.
        You are allowed to repeatedly remove any substring where the number of 'a' characters is equal to the number of 'b' characters.
        After each removal, the remaining parts of the string are concatenated together without gaps.
        Return an integer denoting the minimum possible length of the string after performing any number of such operations.

        Example 1:
        Input: s = "aabbab"
        Output: 0

        Explanation:
        The substring "aabbab" has three 'a' and three 'b'. Since their counts are equal, we can remove the entire string directly. The minimum length is 0.

        Example 2:
        Input: s = "aaaa"

        Output: 4
        Explanation:
        Every substring of "aaaa" contains only 'a' characters. No substring can be removed as a result, so the minimum length remains 4.

        Constraints:

        1 <= s.length <= 10^5
        s[i] is either 'a' or 'b'
    '''
    def minLengthAfterRemovals(self, s: str) -> int:
        a=s.count('a');b=len(s)-a
        return abs(a-b)
    '''
    3747. Count Distinct Integers After Removing Zeros
    You are given a positive integer n.
    For every integer x from 1 to n, we write down the integer obtained by removing all zeros from the decimal representation of x.
    Return an integer denoting the number of distinct integers written down.

    Example 1:
    Input: n = 10
    Output: 9
    Explanation:
    The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).

    Constraints:
    1 <= n <= 10^15
    '''
    def countDistinct(self, n: int) -> int:
        digits=[int(dgt) for dgt in str(n)]
        l=len(digits); fn=lambda N:-1+((9**(N)-1)//(9-1))
        i=0;res=fn(l)+1 # inc by 1 because n is itself unique if not include zero (assumed it not has zero)
        while i<l:
            if not digits[i]: 
                res-=1; break # it had zero, pre-assumption was false! 
            res+=(digits[i]-1)*(9**(l-i-1))
            i+=1
        return res
    '''
    3748. Count Stable Subarrays
    You are given an integer array nums.
    A subarray of nums is called stable if it contains no inversions, i.e., there is no pair of indices i < j such that nums[i] > nums[j].
    You are also given a 2D integer array queries of length q, where each queries[i] = [li, ri] represents a query. For each query [li, ri], compute the number of stable subarrays that lie entirely within the segment nums[li..ri].
    Return an integer array ans of length q, where ans[i] is the answer to the ith query.​​​​​​​​​​​​​​
    Note:
    A single element subarray is considered stable.
    
    Example 1:
    Input: nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]
    Output: [2,3,4]

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= queries.length <= 10^5
    queries[i] = [li, ri]
    0 <= li <= ri <= nums.length - 1
    '''
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n=len(nums);toright=[1]*n;toleft=[0]*n;prefix=[1]*n
        for i in range(1,n):
            if nums[i]>=nums[i-1]: toright[i]+=toright[i-1]
            prefix[i]=prefix[i-1]+toright[i]
            j=n-i-1
            if nums[j]<=nums[j+1]: toleft[j]+=max(1,toleft[j+1])
        # print(f'toright={toright} toleft={toleft} prefix={prefix}')
        for i,[l,r] in enumerate(queries):
            queries[i]=prefix[r]-prefix[l]-(toright[l]-1)*min(toleft[l],r-l)+1
        return queries