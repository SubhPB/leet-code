from typing import List
from bisect import bisect_left as bl    

class Solution:
    '''
    165. Compare Version Numbers
    Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
    To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
    Return the following:
    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.
    
    Example 1:

    Input: version1 = "1.2", version2 = "1.10"

    Output: -1

    Explanation:

    version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

    Example 2:

    Input: version1 = "1.01", version2 = "1.001"

    Output: 0

    Explanation:

    Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

    Example 3:

    Input: version1 = "1.0", version2 = "1.0.0.0"

    Output: 0

    Explanation:

    version1 has less revisions, which means every missing revision are treated as "0".

    Constraints:

    1 <= version1.length, version2.length <= 500
    version1 and version2 only contain digits and '.'.
    version1 and version2 are valid version numbers.
    All the given revisions in version1 and version2 can be stored in a 32-bit integer.
    '''
    def compareVersion(self, v1: str, v2: str) -> int:
        [v1,v2] = [v.split('.') for v in (v1,v2)]
        n1=len(v1);n2=len(v2)
        for i in range(max(n1,n2)):
            x = int(v1[i]) if i<n1 else 0
            y = int(v2[i]) if i<n2 else 0
            if x>y: return 1
            elif y>x: return -1
        return 0
    ''' Q120
    Given a triangle array, return the minimum path sum from top to bottom.
    For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

    Example 1:

    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
    2
    3 4
    6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
    Example 2:

    Input: triangle = [[-10]]
    Output: -10
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Main challenge was to solve in O(n) space complexity!
        dp = list(triangle[-1]); n = len(triangle)
        for row in range(n-2,-1,-1):
            for col in range(row+1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col+1])
        return dp[0]
    '''
    611. Valid Triangle Number
    Given an integer array nums, return the number of triplets chosen from the array that can make triangles
    if we take them as side lengths of a triangle.

    Example 1:

    Input: nums = [2,2,3,4]
    Output: 3
    Explanation: Valid combinations are: 
    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3
    
    Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000
    '''
    def triangleNumber(self, nums: List[int]) -> int:
        res=0;n=len(nums);nums.sort()
        for l in range(n-1):
            for r in range(l+1,n):
                a=nums[l];b=nums[r]
                l = bl(nums,a+b)
                # l, <...déjàCompté>, r, <...ilFautCompter>, l, ...
                res+=max(0,l-r-1)
        return res