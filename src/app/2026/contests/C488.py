from typing import List
class Solution:
    '''
    3834. Merge Adjacent Equal Elements
    You are given an integer array nums.
    You must repeatedly apply the following merge operation until no more changes can be made:
    If any two adjacent elements are equal, choose the leftmost such adjacent pair in the current array and replace them with a single element equal to their sum.
    After each merge operation, the array size decreases by 1. Repeat the process on the updated array until no more changes can be made.
    Return the final array after all possible merge operations.
    
    Example 1:
    Input: nums = [3,1,1,2]
    Output: [3,4]
    Explanation:
    The middle two elements are equal and merged into 1 + 1 = 2, resulting in [3, 2, 2].
    The last two elements are equal and merged into 2 + 2 = 4, resulting in [3, 4].
    No adjacent equal elements remain. Thus, the answer is [3, 4].

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5​​​​​​​
    '''
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        n=len(nums);x=1;i=1
        while i<n:
            if nums[i]!=nums[x-1]:
                nums[x]=nums[i]; x+=1
            else:
                nums[x-1]*=2
            while x>1 and nums[x-1]==nums[x-2]:
                x-=1; nums[x-1]*=2
            i+=1
        return nums[:x]
    '''
    3835. Count Subarrays With Cost Less Than or Equal to K

    You are given an integer array nums, and an integer k.
    For any subarray nums[l..r], define its cost as:
    cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1).
    Return an integer denoting the number of subarrays of nums whose cost is less than or equal to k.

    Example 1:
    Input: nums = [1,3,2], k = 4
    Output: 5
    Explanation:

    We consider all subarrays of nums:
    nums[0..0]: cost = (1 - 1) * 1 = 0
    nums[0..1]: cost = (3 - 1) * 2 = 4
    nums[0..2]: cost = (3 - 1) * 3 = 6
    nums[1..1]: cost = (3 - 3) * 1 = 0
    nums[1..2]: cost = (3 - 2) * 2 = 2
    nums[2..2]: cost = (2 - 2) * 1 = 0
    There are 5 subarrays whose cost is less than or equal to 4.

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= k <= 10^15
    '''
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Solved something that was not asked!...
        n=len(nums); nums.append(0); res=0
        for i in range(n):
            nums[i]+=nums[i-1]
            if nums[i]-nums[i-1]<=k:
                l=0;r=i+1
                while l<r:
                    m=(l+r)//2; sk=nums[i]-nums[m-1]
                    if sk>k: l=m+1
                    else: r=m
                res+=((i-l+1)*(i-l+2))//2
        return res
    '''
    3836. Maximum Score Using Exactly K Pairs

    You are given two integer arrays nums1 and nums2 of lengths n and m respectively, and an integer k.
    You must choose exactly k pairs of indices (i1, j1), (i2, j2), ..., (ik, jk) such that:
    0 <= i1 < i2 < ... < ik < n
    0 <= j1 < j2 < ... < jk < m
    For each chosen pair (i, j), you gain a score of nums1[i] * nums2[j].
    The total score is the sum of the products of all selected pairs.
    Return an integer representing the maximum achievable total score.

    Example 1:
    Input: nums1 = [1,3,2], nums2 = [4,5,1], k = 2
    Output: 22
    Explanation:
    One optimal choice of index pairs is:
    (i1, j1) = (1, 0) which scores 3 * 4 = 12
    (i2, j2) = (2, 1) which scores 2 * 5 = 10
    This gives a total score of 12 + 10 = 22.

    Constraints:
    1 <= n == nums1.length <= 100
    1 <= m == nums2.length <= 100
    -106 <= nums1[i], nums2[i] <= 10^6
    1 <= k <= min(n, m)
    '''
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1);m=len(nums2);inf=10**15
        dp=[
            [0 if x!=n and y!=m else -inf for y in range(m+1)] for x in range(n+1)
        ]
        for z in range(1,k+1):
            temp=[[*row] for row in dp]
            for x in range(n,-1,-1):
                for y in range(m,-1,-1):
                    if x+z<=n and y+z<=m:
                        temp[x][y]=max(
                            nums1[x]*nums2[y]+(dp[x+1][y+1] if z>1 else 0),
                            temp[x+1][y],
                            temp[x][y+1]
                        )
                    else:
                        temp[x][y]=-inf
            dp=temp
        return dp[0][0]