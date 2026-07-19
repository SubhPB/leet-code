import math
class Solution:
    '''
    3951. Minimum Energy to Maintain Brightness
    You are given an integer n, representing n light bulbs arranged in a line and indexed from 0 to n - 1.
    You are also given an integer brightness and a 2D integer array intervals, where intervals[i] = [starti, endi] represents an inclusive time interval during which the lighting requirement must be satisfied.
    At each time unit, every bulb can independently be either on or off. A bulb that is on illuminates its own position and its adjacent positions, if they exist.
    The total illumination at a time unit is the number of illuminated positions. Each position is counted at most once.
    For every integer time unit covered by at least one interval in intervals, the total illumination must be at least brightness. At time units not covered by any interval, all bulbs may remain off. Each bulb that is on consumes 1 unit of energy for that time unit.
    Return an integer denoting the minimum total energy required.

    Example 1:
    Input: n = 5, brightness = 5, intervals = [[6,12]]
    Output: 14
    Explanation:
    Turn on the light bulbs at positions 1 and 4.
    Current state of line: 0 1 0 0 1.
    All 5 positions are illuminated, so the required brightness is reached.
    The active interval has length 12 - 6 + 1 = 7, so the total energy is 2 * 7 = 14.

    Constraints:
    1 <= n <= 10**6
    1 <= brightness <= n
    1 <= intervals.length <= 10**5
    intervals[i] == [starti, endi]
    0 <= starti <= endi <= 10**9
    '''
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        # incomplete
        intervals.sort(key=lambda interval:(interval[0],-interval[1]))
        pstart,pend=intervals[0]
        t=pend-pstart+1; i=1
        while i<len(intervals):
            start,end=intervals[i]
            if start>pend:
                t+=end-start+1
            elif end>pend:
                t+=end-pend
            pstart,pend=start,max(pend,end)
            i+=1
        return t*math.ceil(brightness/3)
    '''
    3952. Maximum Total Value of Covered Indices
    You are given an integer array nums of length n and a binary string s of length n, where s[i] == '1' means index i initially contains a token and s[i] == '0' means it does not.
    You may perform the following operation any number of times:
    Choose a token currently located at index i, where i > 0, such that this token has not been moved before.
    Move this token from index i to index i - 1.
    An index is considered covered if it contains a token after all moves.
    Return an integer denoting the maximum total value of nums at the covered indices after optimally performing the operations.

    Example 1:
    Input: nums = [9,2,6,1], s = "0101"
    Output: 15
    Explanation:
    Initially, indices 1 and 3 contain tokens.
    Move the token from index 3 to index 2.
    Move the token from index 1 to index 0.
    The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 6 = 15.
    
    Constraints:
    1 <= n == nums.length == s.length <= 10**5
    1 <= nums[i] <= 10**5
    ​​​​​​​s[i] is either '0' or '1'
    '''
    def maxTotal(self, nums: list[int], s: str) -> int:
        n=len(nums);i=0;res=0
        while i<n:
            res+=nums[i]
            if not int(s[i]):
                j=i+1;mn=nums[i]
                while j<n and int(s[j]):
                    mn=min(mn,nums[j])
                    res+=nums[j]
                    j+=1
                res-=mn
                i=j-1
            i+=1
        return res
    '''
    3953. Maximum Score with Co-Prime Element

    You are given an integer array nums of length n and an integer maxVal.
    You may change any element in nums to any positive integer less than or equal to maxVal. Each such change costs 1.
    Two integers are co-prime if their greatest common divisor (GCD) is 1.
    After all modifications, you must choose an index i such that, nums[i] is co-prime with every other element nums[j].
    Let:
    selectedValue be the final value of nums[i] after modifications.
    modificationCost be the total number of elements changed.
    The score is defined as score = selectedValue - modificationCost.

    Return the maximum possible score.

    Example 1:
    Input: nums = [3,4,6], maxVal = 5
    Output: 4

    Explanation:
    Change nums[2] from 6 to 5, which costs 1. Choose nums[2] = 5, since it is co-prime with 3 and 4.

    selectedValue = 5
    modificationCost = 1
    The score is 5 - 1 = 4

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**5
    1 <= maxVal <= 10**​​​​​​​5
    '''
    def maxScore(self, nums: list[int], maxVal: int) -> int:
        # incomplete
        pass