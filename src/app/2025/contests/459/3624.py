'''
    3624. Number of Integers With Popcount-Depth Equal to K II

    You are given an integer array nums.

    For any positive integer x, define the following sequence:

    p0 = x
    pi+1 = popcount(pi) for all i >= 0, where popcount(y) is the number of set bits (1's) in the binary representation of y.
    This sequence will eventually reach the value 1.

    The popcount-depth of x is defined as the smallest integer d >= 0 such that pd = 1.

    For example, if x = 7 (binary representation "111"). Then, the sequence is: 7 → 3 → 2 → 1, so the popcount-depth of 7 is 3.

    You are also given a 2D integer array queries, where each queries[i] is either:

    [1, l, r, k] - Determine the number of indices j such that l <= j <= r and the popcount-depth of nums[j] is equal to k.
    [2, idx, val] - Update nums[idx] to val.
    Return an integer array answer, where answer[i] is the number of indices for the ith query of type [1, l, r, k].

    

    Example 1:

    Input: nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]

    Output: [2,1]

    Example 2:

    Input: nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]

    Output: [3,1,0]

    Example 3:

    Input: nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]

    Output: [1,0,1]
    

    Constraints:

    1 <= n == nums.length <= 105
    1 <= nums[i] <= 10^15
    1 <= queries.length <= 10^5
    queries[i].length == 3 or 4
    queries[i] == [1, l, r, k] or,
    queries[i] == [2, idx, val]
    0 <= l <= r <= n - 1
    0 <= k <= 5
    0 <= idx <= n - 1
    1 <= val <= 10^15

    python ./src/app/2025/contests/459/3624.py
'''

from functools import cache
from collections import defaultdict

@cache
def cntDepth(x:int):
    cnt = x.bit_count()
    return 1+cntDepth(cnt) if cnt>=1 and x>1 else 0

class Solution:
    def popcountDepth(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        depths = defaultdict(list)
        [depths[cntDepth(num)].append(i) for i, num in enumerate(nums)]

        def getIndices(left:int,right:int,depth:int):
            depth = depths[depth]
            if depth and left<=depth[-1] and right>=depth[0]:
                l,r = 0, len(depth)-1
                while l<r:
                    m = (l+r)//2
                    if depth[m] >= left:
                        r = m
                    else:
                        l = m+1
                leftBoundary = l
                l,r = 0, len(depth)-1
                while l<r:
                    m = (l+r+1)//2
                    if depth[m] <= right:
                        l = m
                    else:
                        r = m-1
                rightBoundary = l
                return rightBoundary-leftBoundary+1
            return 0
        
        res = []
        for query in queries:
            if query[0]==1:
                [_,l,r,k] = query
                res.append(getIndices(l,r,k))
            else:
                [_,idx,val] = query
                [prevK, newK] = [cntDepth(x) for x in [nums[idx], val]]
                if prevK != newK:
                    
                    depth = depths[prevK]
                    left, right = 0, len(depth)-1

                    while left<right:#deleting idx from depths[prevK]
                        m = (left+right)//2
                        if depth[m] == idx:
                            left=m
                            right=m
                        elif depth[m]<idx:
                            right = m-1
                        else: left = m+1
                    depths[prevK] = depths[prevK][:left] + depths[prevK][left+1:]

                    depth = depths[newK]
                    if not depth or idx < depth[0]: 
                        depths[newK] = [idx]+depths[newK]
                    elif depth[-1] < idx:
                        depths[newK].append(idx)
                    else:
                        left, right = 0, len(depth)-1
                        while left<right:
                            m = (left+right)//2
                            if idx<depth[m]:
                                right = m
                            else:
                                left = m+1
                        depths[newK] = depths[newK][:l] + [idx] + depths[newK][l:]
                    
                    nums[idx] = val
        return res
if __name__ == "__main__":
    testcases = []
    add = lambda nums,queries : testcases.append([nums,queries])
    # add(nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]])
    # add(nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]])
    # add(nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]])
    add(nums=[8], queries=[[2,0,8],[1,0,0,2],[2,0,5],[1,0,0,4],[2,0,9],[2,0,9],[1,0,0,2],[2,0,10],[1,0,0,5],[1,0,0,0]])

    for [nums,queries] in testcases:
        print(f'Nums={nums} queries={queries} result={Solution().popcountDepth(nums,queries)}')