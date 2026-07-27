import heapq

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
    '''
    3962. Maximum Subarray Sum After at Most K Swaps

    You are given an integer array nums and an integer k.
    You are allowed to perform at most k swap operations on the array.
    In one swap operation, you may choose any two indices i and j and swap nums[i] and nums[j].
    Return an integer denoting the maximum possible subarray sum after performing the swaps.

    Example 1:
    Input: nums = [1,-1,0,2], k = 1
    Output: 3
    Explanation:
    We can swap on indices 1 and 3, resulting in the array [1, 2, 0, -1].
    The subarray [1, 2] has a sum of 3, which is the maximum possible subarray sum after at most k = 1​​​​​​​ swap.

    Constraints:
    1 <= nums.length <= 1500
    -10**5 <= nums[i] <= 10**5
    0 <= k <= nums.length
    '''
    def maxSum(self, nums: list[int], k: int) -> int:
        n=len(nums); res=-10**18

        if k==0 or n==1:
            sm=0
            for x in nums:
                sm+=x
                res=max(res,sm)
                if sm<0: sm=0
            return res
        

        cnt=0; curr_nonneg_sm=0
        pref=[0]*(n+1)

        for i in range(n):
            if nums[i]>=0:
                curr_nonneg_sm+=nums[i]
            else:
                cnt+=1
            pref[i+1]=pref[i]+nums[i]
            res=max(res,nums[i])
        
        if cnt<=k and cnt!=n: # no of negative ints are less or equal to swaps 
            return curr_nonneg_sm
        
        # dp[i][j] = sum of k smallest negatives in [i..j]
        dp=[[0]*n for _ in range(n)]
        
        for i in range(n):
            pq=[];sm=0
            for j in range(i,n):
                if nums[j]>=0:
                    dp[i][j]=sm # sm of negative elements in btw [i..j] 
                elif len(pq)<k:
                    heapq.heappush(pq,-nums[j])
                    sm+=nums[j]
                else:
                    if -pq[0]>nums[j]:
                        sm-=-pq[0]
                        heapq.heapreplace(pq,-nums[j])
                        sm+=nums[j]
        for i in range(n):
            pq=[] # min-heap for up to k largest positives
            sm=0 # sum of positive k elements

            # left-> [0,i-1]
            for j in range(i):
                if nums[j]<0: continue
                elif len(pq)<k:
                    heapq.heappush(pq,nums[j])
                    sm+=nums[j]
                else:
                    if pq[0]<nums[j]:
                        sm-=pq[0]
                        heapq.heapreplace(pq,nums[j])
                        sm+=nums[j]

            # right side [i+1..n+1]
            for j in range(n-1,i,-1):
                curr=pref[j+1]-pref[i] 
                curr-=dp[i][j] #subtract selected negatives
                curr+=sm
                res=max(res,curr)

                if nums[j]<0: continue
                if len(pq)<k:
                    heapq.heappush(pq,nums[j])
                    sm+=nums[j]
                else:
                    if pq[0]<nums[j]:
                        sm-=pq[0]
                        heapq.heapreplace(pq,nums[j])
                        sm+=nums[j]
                if pq: res=max(res,sm)
        return res
