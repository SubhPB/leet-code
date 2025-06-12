'''
3578. Count Partitions With Max-Min Difference at Most K

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 

Constraints:

2 <= nums.length <= 5 * 104
1 <= nums[i] <= 109
0 <= k <= 109
'''

from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n, mod = len(nums), 10**9+7
        '''
        dp[i] represents how many ways nums can be partitioned when last element of the segment is nums[i-1]
        So dp[0] may not really make sense and dp[-1] holds our final answer
        '''
        dp = [0]*(n+1)
        dp[0]=1
        '''
        prefix[i] = dp[0] + dp[1] + ... + dp[i-1]
        '''
        prefix = [0]*(n+2)
        prefix[1] = dp[0]

        def modadd(*x):
            res=0
            for v in x: res = (res%mod+v%mod)%mod
            return res

        left=0
        maxdeq, mindeq = deque(), deque()
        for right in range(n):
            #remove the old mins and max values
            while len(maxdeq) and maxdeq[0]<left: maxdeq.popleft()
            while len(mindeq) and mindeq[0]<left: mindeq.popleft()

            while len(maxdeq) and nums[maxdeq[-1]]<=nums[right]: maxdeq.pop()
            while len(mindeq) and nums[mindeq[-1]]>=nums[right]: mindeq.pop()
            maxdeq.append(right)
            mindeq.append(right)

            diff = nums[maxdeq[0]]-nums[mindeq[0]]
            while diff>k:
                if maxdeq[0]==left: maxdeq.popleft()
                if mindeq[0]==left: mindeq.popleft()
                left+=1
                diff = nums[maxdeq[0]]-nums[mindeq[0]]
            
            #Here we've found a segment that starts at position[left] and whose last index at position[right]
            dp[right+1] = modadd(0, prefix[right+1]-prefix[left])
            prefix[right+2] = modadd(prefix[right+1],dp[right+1])


        return dp[-1]
    


