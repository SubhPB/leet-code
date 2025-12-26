import heapq
from typing import List

'''^^^^^^^^^^^^^^^^^^^^^^#3782^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
maxn=10**15; maxops=(maxn-1).bit_length(); cache=[1]*(maxops+1)
for i in range(1,maxops+1): cache[i]=2*cache[i-1]

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
    '''
    3782. Last Remaining Integer After Alternating Deletion Operations
    You are given an integer n.
    We write the integers from 1 to n in a sequence from left to right. Then, alternately apply the following two operations until only one integer remains, starting with operation 1:
    Operation 1: Starting from the left, delete every second number.
    Operation 2: Starting from the right, delete every second number.
    Return the last remaining integer.

    Example 1:
    Input: n = 8
    Output: 3
    Explanation:

    Write [1, 2, 3, 4, 5, 6, 7, 8] in a sequence.
    Starting from the left, we delete every second number: [1, 2, 3, 4, 5, 6, 7, 8]. The remaining integers are [1, 3, 5, 7].
    Starting from the right, we delete every second number: [1, 3, 5, 7]. The remaining integers are [3, 7].
    Starting from the left, we delete every second number: [3, 7]. The remaining integer is [3].

    Constraints:
    1 <= n <= 10^15
    '''
    def lastInteger(self, n: int) -> int:
        l=1;r=n;x=0
        while l!=r:
            q=(r-l)//cache[x]
            if q%2: # odd -> delete
                if x%2: #rtl
                    l+=cache[x]
                else: #ltr
                    r-=cache[x]
            x+=1
        return l 