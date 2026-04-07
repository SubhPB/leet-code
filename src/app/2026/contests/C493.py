from typing import List
class Solution:
    '''
    3871. Count Commas in Range II
    You are given an integer n.
    Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
    In standard formatting:
    A comma is inserted after every three digits from the right.
    Numbers with fewer than 4 digits contain no commas.

    Example 1:
    Input: n = 1002
    Output: 3
    Explanation:
    The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

    Constraints:
    1 <= n <= 10^15
    '''
    def countCommas(self, n: int) -> int:
        r=0; thl=[10**3,10**6,10**9,10**12,10**15]
        for t in thl:
            if n>=t: r+=n-(t-1)
        return r
    '''
    3872. Longest Arithmetic Sequence After Changing At Most One Element
    You are given an integer array nums.
    A subarray is arithmetic if the difference between consecutive elements in the subarray is constant.
    You can replace at most one element in nums with any integer. Then, you select an arithmetic subarray from nums.
    Return an integer denoting the maximum length of the arithmetic subarray you can select.

    Example 1:

    Input: nums = [9,7,5,10,1]
    Output: 5

    Explanation:
    Replace nums[3] = 10 with 3. The array becomes [9, 7, 5, 3, 1].
    Select the subarray [9, 7, 5, 3, 1], which is arithmetic because consecutive elements have a common difference of -2.
    Example 2:


    Constraints:
    4 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    '''
    def longestArithmetic(self, e: List[int]) -> int:
        n=len(e); res=0; seg=[2]*n; seg[0]=1; seg[-1]=1
        for i in range(2,n-1):
            if e[i]-e[i-1]==e[i-1]-e[i-2]:
                seg[i]=1+seg[i-1]
        for i in range(n-1,-1,-1):
            res=max(
                res,
                1+ seg[i-1] if i>0 else 0,
                1+ seg[i+1] if i<n-1 else 0,
                1+ (seg[i-1]+seg[i+1]) if 0<i<n-1 and not (e[i-1]-e[i+1])%2 else 0
            )
            if i<n-2 and e[i+2]-e[i+1]==e[i+1]-e[i]:
                seg[i]=1+seg[i+1]
            elif i==n-2: seg[i]=2
        return res
    '''
    3873. Maximum Points Activated with One Addition

    You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point. All coordinates in points are distinct.
    If a point is activated, then all points that have the same x-coordinate or y-coordinate become activated as well.
    Activation continues until no additional points can be activated.
    You may add one additional point at any integer coordinate (x, y) not already present in points. Activation begins by activating this newly added point.
    Return an integer denoting the maximum number of points that can be activated, including the newly added point.

    Example 1:
    Input: points = [[1,1],[1,2],[2,2]]
    Output: 4
    Explanation:
    Adding and activating a point such as (1, 3) causes activations:
    (1, 3) shares x = 1 with (1, 1) and (1, 2) -> (1, 1) and (1, 2) become activated.
    (1, 2) shares y = 2 with (2, 2) -> (2, 2) becomes activated.
    Thus, the activated points are (1, 3), (1, 1), (1, 2), (2, 2), so 4 points in total. We can show this is the maximum activated.

    Constraints:
    1 <= points.length <= 10^5
    points[i] = [xi, yi]
    -10^9 <= xi, yi <= 10^9
    points contains all distinct coordinates.
    '''
    def maxActivated(self, points: list[list[int]]) -> int:
        pass