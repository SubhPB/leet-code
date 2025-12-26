import heapq
from typing import List
class Solution:
    '''
    3780. Maximum Sum of Three Numbers Divisible by Three

    You are given an integer array nums.
    Your task is to choose exactly three integers from nums such that their sum is divisible by three.
    Return the maximum possible sum of such a triplet. If no such triplet exists, return 0.

    Example 1:
    Input: nums = [4,2,3,1]
    Output: 9

    Explanation:
    The valid triplets whose sum is divisible by 3 are:

    (4, 2, 3) with a sum of 4 + 2 + 3 = 9.
    (2, 3, 1) with a sum of 2 + 3 + 1 = 6.
    Thus, the answer is 9.

    Constraints:
    3 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    '''
    def maximumSum(self, nums: List[int]) -> int:
        G:List[List[int]]=[[] for i in range(3)]; res=0
        nums.sort(key=lambda x:-x)
        for num in nums: G[num%3].append(num)
        for r in range(3): # (0,0,0); (1,1,1); (2,2,2)
            if len(G[r])>=3: res=max(res,sum(G[r][i] for i in range(3)))
        if all(len(G[r])>0 for r in range(3)): # (0,1,2)
            res=max(res,sum(G[r][0] for r in range(3)))
        return res
    '''
    3781. Maximum Score After Binary Swaps

    You are given an integer array nums of length n and a binary string s of the same length.
    Initially, your score is 0. Each index i where s[i] = '1' contributes nums[i] to the score.
    You may perform any number of operations (including zero). In one operation, you may choose an index i such that 0 <= i < n - 1, where s[i] = '0', and s[i + 1] = '1', and swap these two characters.
    Return an integer denoting the maximum possible score you can achieve.

    Example 1:
    Input: nums = [2,1,5,2,3], s = "01010"
    Output: 7

    Explanation:
    We can perform the following swaps:

    Swap at index i = 0: "01010" changes to "10010"
    Swap at index i = 2: "10010" changes to "10100"
    Positions 0 and 2 contain '1', contributing nums[0] + nums[2] = 2 + 5 = 7. This is maximum score achievable.

    Constraints:
    n == nums.length == s.length
    1 <= n <= 10^5
    1 <= nums[i] <= 10^9
    s[i] is either '0' or '1'
    '''
    def maximumScore(self, nums: List[int], s: str) -> int:
        hq=[]; n=len(nums); res=0
        for i in range(n):
            heapq.heappush(hq,-nums[i])
            if int(s[i]): res-=heapq.heappop(hq)
        return res