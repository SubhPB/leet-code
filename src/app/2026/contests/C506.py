class Solution:
    '''
    3960. Frequency Balance Subarray

    You are given an integer array ​​​​​​​nums.
    Define a frequency balance subarray as follows:
    If the subarray contains only one distinct value, it is frequency balanced.
    Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times, and both frequencies occur among the distinct values.
    Return an integer denoting the length of the longest frequency balance subarray.

    Example 1:
    Input: nums = [1,2,2,1,2,3,3,3]
    Output: 5
    Explanation:
    The longest frequency balance subarray is [2, 1, 2, 3, 3].
    The elements that appear most frequently are 2 and 3, both appearing twice.
    The remaining element 1 appears once, meeting the requirements.

    Constraints:
    1 <= nums.length <= 10**​​​​​​​3
    1 <= nums[i] <= 10**​​​​​​​9
    '''
    def getLength(self, nums: list[int]) -> int:
        n=len(nums); res=1
        for i in range(n):
            freq={};freqCount={}
            for j in range(i,n):
                old=freq.get(nums[j],0)
                if old: 
                    freqCount[old]-=1
                    if not freqCount[old]:
                        del freqCount[old]
                        
                if nums[j] not in freq:
                    freq[nums[j]]=0
                freq[nums[j]]+=1
                newfreq=freq.get(nums[j],0)
                if newfreq not in freqCount:
                    freqCount[newfreq]=0
                freqCount[newfreq]+=1

                if len(freq)==1:
                    res=max(res,j-i+1)
                elif len(freqCount)==2:
                    f1,f2=sorted(freqCount)
                    if f2==2*f1:
                        res=max(res,j-i+1)
        return res
    '''
    3961. Maximize Sum of Device Ratings

    You are given a 2D integer array units of size m × n where units[i][j] represents the capacity of the jth unit in the ith device. Each device contains exactly n units.
    The rating of a device is the minimum capacity among all its units.
    You may perform the following operation any number of times (including zero):
    Choose a device i that has not been used as a source before.
    Remove exactly one unit from device i and add it to any different device.
    Then mark device i as used, so it cannot be chosen again as a source.
    Return the maximum possible sum of the ratings of all devices after any number of such operations.
    Note:
    Devices can receive units from multiple devices, regardless of whether they have been selected.
    The rating of an empty device is 0.

    Example 1:
    Input: units = [[1,3],[2,2]]
    Output: 4

    Constraints:
    1 <= m == units.length <= 10**5
    1 <= n == units[i].length <= 10**5
    m * n <= 2 * 10**5
    1 <= units[i][j] <= 10**5
    '''
    def maxRatings(self, units: list[list[int]]) -> int:
        inf=10**9+7; res=0
        mn=inf; sm=0; vmn=inf

        for i,unit in enumerate(units):
            m=len(unit)
            v1=unit[0]
            v2=inf
            mx=v1
            if m-1:
                for j in range(1,m):
                    if unit[j]<v2:
                        v2=unit[j]
                    if v2<v1:
                        v1,v2=v2,v1
                    mx=max(mx,unit[j])
            else:
                v2=v1
                vmn=min(vmn,v1)
                
            mn=min(mn,v1)
            res+=v1
            units[i]=[mx,v2,v1]
            sm+=v2

        for [mx,v2,v1] in units:
            res=max(
                res, sm-v2+mn
            )
            res=max(
                res,
                (sm-v2+mn)-vmn+mx
            )
        return res

