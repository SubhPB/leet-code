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
