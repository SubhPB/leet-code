from typing import List
class Solution:
    '''
    3795. Minimum Subarray Length With Distinct Sum At Least K
    You are given an integer array nums and an integer k.
    Return the minimum length of a subarray whose sum of the distinct values present in that subarray (each value counted once) is at least k. If no such subarray exists, return -1.
    
    Example 1:
    Input: nums = [2,2,3,1], k = 4
    Output: 2
    Explanation:
    The subarray [2, 3] has distinct elements {2, 3} whose sum is 2 + 3 = 5, which is ​​​​​​​at least k = 4. Thus, the answer is 2.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= k <= 10^9
    '''
    def minLength(self, nums: List[int], k: int) -> int:
        n=len(nums); res=n+1; s={}
        i=0;j=0;t=0
        while j<=n:
            if t>=k:
                res=min(res,j-i)
                s[nums[i]]-=1
                if not s[nums[i]]: 
                    del s[nums[i]]; t-=nums[i]
                i+=1
            else:
                if j<n:
                    if nums[j] not in s:
                        s[nums[j]]=0; t+=nums[j]
                    s[nums[j]]+=1
                j+=1
        return res if res<=n else -1
    '''
    3796. Find Maximum Value in a Constrained Sequence
    You are given an integer n, a 2D integer array restrictions, and an integer array diff of length n - 1.
    Your task is to construct a sequence of length n, denoted by a[0], a[1], ..., a[n - 1], such that it satisfies the following conditions:
    a[0] is 0.All elements in the sequence are non-negative.
    For every index i (0 <= i <= n - 2), abs(a[i] - a[i + 1]) <= diff[i].
    For each restrictions[i] = [idx, maxVal], the value at position idx in the sequence must not exceed maxVal (i.e., a[idx] <= maxVal).
    Your goal is to construct a valid sequence that maximizes the largest value within the sequence while satisfying all the above conditions.
    Return an integer denoting the largest value present in such an optimal sequence.

    Example 1:
    Input: n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2]
    Output: 6
    Explanation:
    The sequence a = [0, 2, 4, 1, 2, 6, 2, 1, 1, 3] satisfies the given constraints (a[3] <= 1 and a[8] <= 1).
    The maximum value in the sequence is 6.

    Constraints:
    2 <= n <= 10^5; 1 <= restrictions.length <= n - 1
    restrictions[i].length == 2; restrictions[i] = [idx, maxVal]
    1 <= idx < n; 1 <= maxVal <= 10^6
    diff.length == n - 1; 1 <= diff[i] <= 10
    The values of restrictions[i][0] are unique.
    '''
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        inf=10**9+7; a=[inf]*(n); a[0]=0
        for [idx,val] in restrictions: a[idx]=val
        for idx in range(1,n): a[idx]=min(
            a[idx],a[idx-1]+diff[idx-1]
        )
        for idx in range(n-2,-1,-1): a[idx]=min(
            a[idx],a[idx+1]+diff[idx]
        )
        # using a[0] as res, just to avoid initializing an extra variable.
        for num in a: a[0]=max(a[0],num)
        return a[0]