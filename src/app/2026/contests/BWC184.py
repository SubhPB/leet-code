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
        intervals.sort(key=lambda interval:(interval[0],-interval[1]))
        pstart,pend=intervals[0]
        t=pend-pstart+1; i=1
        while i<len(intervals):
            start,end=intervals[i]
            if start>pend:
                t+=end-start+1
            elif end>pend:
                t+=end-pend
            pstart,pend=start,end
            i+=1
        return t*math.ceil(brightness/3)

            