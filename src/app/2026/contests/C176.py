from typing import List
class Solution:
    '''
    3810. Minimum Operations to Reach Target Array

    You are given two integer arrays nums and target, each of length n, 
    where nums[i] is the current value at index i and target[i] is the desired value at index i.
    You may perform the following operation any number of times (including zero):
    Choose an integer value x
    Find all maximal contiguous segments 
    where nums[i] == x (a segment is maximal if it cannot be extended to the left or right while keeping all values equal to x)
    For each such segment [l, r], update simultaneously:
    nums[l] = target[l], nums[l + 1] = target[l + 1], ..., nums[r] = target[r]
    Return the minimum number of operations required to make nums equal to target.

    Example 1:
    Input: nums = [1,2,3], target = [2,1,3]
    Output: 2

    Explanation:​​​​​​​
    Choose x = 1: maximal segment [0, 0] updated -> nums becomes [2, 2, 3]
    Choose x = 2: maximal segment [0, 1] updated (nums[0] stays 2, nums[1] becomes 1) -> nums becomes [2, 1, 3]
    Thus, 2 operations are required to convert nums to target.​​​​​​​​​​​​​​

    Constraints:
    1 <= n == nums.length == target.length <= 10^5
    1 <= nums[i], target[i] <= 10^5
    '''
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        freq={}; n=len(nums)
        for i in range(n):
            if nums[i]!=target[i]: freq[nums[i]]=1+freq.get(nums[i],0)
        return len(freq)
    '''
    3811. Number of Alternating XOR Partitions

    You are given an integer array nums and two distinct integers target1 and target2.
    A partition of nums splits it into one or more contiguous, non-empty blocks that cover the entire array without overlap.
    A partition is valid if the bitwise XOR of elements in its blocks alternates between target1 and target2, starting with target1.
    Formally, for blocks b1, b2, …:

    XOR(b1) = target1
    XOR(b2) = target2 (if it exists)
    XOR(b3) = target1, and so on.
    Return the number of valid partitions of nums, modulo 109 + 7.
    Note: A single block is valid if its XOR equals target1.

    Example 1:
    Input: nums = [2,3,1,4], target1 = 1, target2 = 5
    Output: 1
    Explanation:​​​​​​​

    The XOR of [2, 3] is 1, which matches target1.
    The XOR of the remaining block [1, 4] is 5, which matches target2.
    This is the only valid alternating partition, so the answer is 1.

    Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i], target1, target2 <= 10^5
    target1 != target2
    '''
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        xors={0:[-1]}
        x=0; M=10**9+7; n=len(nums)
        add=lambda x,y: (x%M+y%M)%M

        dp=[[0,0] for _ in range(n+1)]
        dp[-1][1]=1 # dp[n:-1][1:tailendsWithXorEqTarget2] : BASECASE

        for i,num in enumerate(nums):
            x^=num; left=x^target1
            # Assuming tail has xor equals target1
            for j in xors.get(left,[]):
                dp[i][0]=add(dp[i][0],dp[j][1])

            left=x^target2
            # Assuming tail ends having xor equals targte2
            for j in xors.get(left,[]):
                dp[i][1]=add(dp[i][1],dp[j][0]) 
            
            if x not in xors: xors[x]=[]
            xors[x].append(i)
        return add(dp[n-1][0], dp[n-1][1])