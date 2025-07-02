'''
3599. Partition Array to Minimize XOR
    You are given an integer array nums and an integer k.

    Your task is to partition nums into k non-empty subarrays. For each subarray, compute the bitwise XOR of all its elements.

    Return the minimum possible value of the maximum XOR among these k subarrays.

    

    Example 1:

    Input: nums = [1,2,3], k = 2

    Output: 1

    Explanation:

    The optimal partition is [1] and [2, 3].

    XOR of the first subarray is 1.
    XOR of the second subarray is 2 XOR 3 = 1.
    The maximum XOR among the subarrays is 1, which is the minimum possible.

    Example 2:

    Input: nums = [2,3,3,2], k = 3

    Output: 2

    Explanation:

    The optimal partition is [2], [3, 3], and [2].

    XOR of the first subarray is 2.
    XOR of the second subarray is 3 XOR 3 = 0.
    XOR of the third subarray is 2.
    The maximum XOR among the subarrays is 2, which is the minimum possible.

    Example 3:

    Input: nums = [1,1,2,3,1], k = 2

    Output: 0

    Explanation:

    The optimal partition is [1, 1] and [2, 3, 1].

    XOR of the first subarray is 1 XOR 1 = 0.
    XOR of the second subarray is 2 XOR 3 XOR 1 = 0.
    The maximum XOR among the subarrays is 0, which is the minimum possible.

    

    Constraints:

    1 <= nums.length <= 250
    1 <= nums[i] <= 109
    1 <= k <= n

    python ./src/app/2025/June/3599.py
'''

class Solution:

    def minXor(self, nums: list[int], k: int) -> int:
        n, inf = len(nums), 10**9
        preXor = [0]*(n+1)
        for i in range(1,n+1): preXor[i] = preXor[i-1]^nums[i-1]

        xor = lambda l,r: preXor[r]^preXor[l]#l points to 'index' but r acts as a length not the last index of sub-array.
        '''
        dp[a][b]: considering only first 'b' elements which are been split into exactly 'a' blocks (a-1 cuts)
                then what is minimum 
        '''
        currDp, prevDp = [inf]*(n+1), [inf]*(n+1)
        #calculating min-max xor for each sub array as one block means zero cut
        for r in range(1, n+1): prevDp[r] = xor(0, r)

        #We know for one block, let's calc min-max xor when 2 blocks are made out for first 'i' elements.
        #and will repeating the process...
        for j in range(2,k+1): 
            for i in range(j, n+1):
                #if we are going to make j cuts then at least we need j elements
                best = inf
                for t in range(j-1,i):
                    best = min(
                        best, max(prevDp[t], xor(t,i))
                    )
                currDp[i]=best
            prevDp = currDp
            currDp = [inf]*(n+1)
        return prevDp[n]
    

if __name__ == "__main__":
    testcases = [
        [[1,2,3], 2],
        [[2,3,3,2], 3],
        [[1,1,2,3,1], 2],
        [[1437,1007,1580,829,287,1762,1060,433,1483,1773], 7]
    ]
    for [nums, k] in testcases:
        print(f'nums={nums} k={k} res={Solution().minXor(nums,k)}')