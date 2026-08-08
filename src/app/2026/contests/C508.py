class Solution:
    '''
    3975. Filter Occupied Intervals

    You are given a 2D integer array occupiedIntervals, where occupiedIntervals[i] = [starti, endi] represents a time interval during which you are occupied. Each interval starts at starti and ends at endi, inclusive. These intervals may overlap.
    You are also given two integers freeStart and freeEnd, which define a free time interval from freeStart to freeEnd, inclusive.
    Your task is to merge all occupied intervals that overlap or touch, then remove all integer points in the free interval from the merged occupied intervals.
    Two intervals touch if the second interval starts immediately after the first one ends. For example, [1, 1] and [2, 2] touch and should be merged into [1, 2].
    Return the remaining occupied intervals in sorted order. The returned intervals must be non-overlapping and must contain the minimum number of intervals possible. If there are no remaining occupied points, return an empty list.

    Example 1:

    Input: occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11
    Output: [[2,6],[12,12],[14,16]]
    Explanation:
    After merging, the occupied intervals are [2, 8], [10, 12], and [14, 16].
    Excluding the free interval [7, 11] results in [2, 6], [12, 12], and [14, 16].

    Constraints:
    1 <= occupiedIntervals.length <= 5 * 10**4
    occupiedIntervals[i].length == 2
    1 <= starti <= endi <= 10**9
    1 <= freeStart <= freeEnd <= 10**9
    '''
    def filterOccupiedIntervals(self, ocpi: list[list[int]], fs: int, fe: int) -> list[list[int]]:
        ocpi.sort(lambda inv:(inv[0],inv[1]))
        res=[]
        for s,e in ocpi:
            ps,pe=res[-1] if res else [-1,-1]
            if s<=pe:
                res[-1][1]=max(pe,e)
            else: 
                res.append([s,e])
        ocpi=[[s,e] for s,e in res]
        res=[]
        for s,e in ocpi:
            if fs<=s<=e<=fe:
                continue
            if e<fs: res.append([s,e])
            elif s>fe: res.append([s,e])
            else:
                if s<fs<=fe<e:
                    res.append([s,fs-1])
                    res.append([fe+1,e])
                elif s<=fs<=fe<e:
                    res.append([fs+1,e])
                elif s<fs<=fe<=e:
                    res.append([s,fe-1])
                elif s<fs:
                    res.append([s,fs-1])
                    if occi[-1][1]<=fe:
                        break
                # elif e< will continue
            
        return res