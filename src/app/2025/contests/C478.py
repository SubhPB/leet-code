from typing import List

class Solution:
    '''
    3762. Minimum Operations to Equalize Subarrays

    You are given an integer array nums and an integer k.
    In one operation, you can increase or decrease any element of nums by exactly k.
    You are also given a 2D integer array queries, where each queries[i] = [li, ri].
    For each query, find the minimum number of operations required to make all elements in the subarray nums[li..ri] equal. If it is impossible, the answer for that query is -1.
    Return an array ans, where ans[i] is the answer for the ith query.

    Example 1:
    Input: nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]
    Output: [1,2]
    Explanation:
    One optimal set of operations:
    i	[li, ri]	nums[li..ri]	Possibility	Operations	Final
    nums[li..ri]	ans[i]
    0	[0, 1]	[1, 4]	Yes	nums[0] + k = 1 + 3 = 4 = nums[1]	[4, 4]	1
    1	[0, 2]	[1, 4, 7]	Yes	nums[0] + k = 1 + 3 = 4 = nums[1]
    nums[2] - k = 7 - 3 = 4 = nums[1]	[4, 4, 4]	2
    Thus, ans = [1, 2].

    Constraints:

    1 <= n == nums.length <= 4 × 10^4
    1 <= nums[i] <= 10^9​​​​​​​
    1 <= k <= 10^9
    1 <= queries.length <= 4 × 10^4
    ​​​​​​​queries[i] = [li, ri]
    0 <= li <= ri <= n - 1
    '''
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n=len(nums);mods=[1]*n
        for i in range(1,n):
            if nums[i]%k == nums[i-1]%k: mods[i]+=mods[i-1]
        for i,[l,r] in enumerate(queries):
            if l-r+1>mods[i]: queries[i]=-1
            else:
                arr=sorted(nums[l:r+1])
                s=0;left=0;right=r-l;lw=1;rw=1
                while arr[left]!=arr[right]:
                    lnext=arr[left+1]//k; rnext=arr[right-1]//k # <- new factor need to add!
                    if rw*rnext<lw*lnext: 
                        s+=rw*rnext; rw+=1; right-=1
                    else:
                        s+=lw*lnext; lw+=1; left+=1
                queries[i]=s
        return queries