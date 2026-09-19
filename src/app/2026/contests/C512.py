import math
class Solution:
    '''
    4001. Aggregate Two Time Series

    You are given two 2D integer arrays series1 and series2.
    Each element in both series is of the form [timestamp, value], where:
    timestamp is an integer representing the time.
    value is an integer representing the value at that timestamp.
    Each array is sorted in strictly increasing order of timestamp.
    For any timestamp not present in a series, its value is taken from the next available timestamp in the same series if one exists. Otherwise, its value is considered 0.
    The aggregated series is formed by summing the corresponding values from both series at every timestamp that appears in either series.
    Return the aggregated series as a 2D integer array of [timestamp, summedValue] pairs, sorted in strictly increasing order of timestamp.

    Example 1:
    Input: series1 = [[1,3],[4,1]], series2 = [[2,2],[5,2]]
    Output: [[1,5],[2,3],[4,3],[5,2]]

    Constraints:
    1 <= series1.length, series2.length <= 10**5
    series1[i].length == series2[i].length == 2
    1 <= series1[i][0], series2[i][0] <= 10**9
    1 <= series1[i][1], series2[i][1] <= 10**9
    Each series is sorted in strictly increasing order of timestamp.
    '''
    def aggregateTimeSeries(self, s1: list[list[int]], s2: list[list[int]]) -> list[list[int]]:
        val1=0;val2=0
        res=[]
        while s1 or s2:
            t=max(
                s[-1][0] for s in (s1,s2) if s
            )
            if s1 and s1[-1][0]==t: val1=s1.pop()[1]
            if s2 and s2[-1][0]==t: val2=s2.pop()[1]
            res.append([t,val1+val2])
        res.reverse()    
        return res
    '''
    4002. Count Valid Sequences

    You are given two positive integers n and k.
    A valid sequence is a sequence of k positive integers such that:
    The sum of all integers in the sequence is equal to n.
    The product of all integers in the sequence is even.
    Return the number of valid sequences. Since the answer may be very large, return it modulo 109​​​​​​​ + 7.
    Two sequences are considered different if they differ at any index. For example, [1, 1, 2] and [1, 2, 1] are considered different sequences.

    Example 1:
    Input: n = 5, k = 3
    Output: 3
    There are 3 sequences with an even product, thus the answer is 3.

    Constraints:
    1 <= n <= 5 * 10**5
    1 <= k <= n
    '''
    def countValidSequences(self, n: int, k: int) -> int:
        mod=10**9+7
        total=math.comb(n-1,k-1)%mod
        odd=0
        if (n-k)%2==0:
            odd=math.comb(
                (n-k)//2 + k-1, k-1
            )%mod
        if (n-k)%2==0:
            odd=math.comb(
                (n-k)//2 +k-1,k-1
            )
        return (total-odd)%mod