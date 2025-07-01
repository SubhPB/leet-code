'''
 * 1498. Number of Subsequences That Satisfy the Given Sum Condition
    You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [3,5,6,7], target = 9
    Output: 4
    Explanation: There are 4 subsequences that satisfy the condition.
    [3] -> Min value + max value <= target (3 + 3 <= 9)
    [3,5] -> (3 + 5 <= 9)
    [3,5,6] -> (3 + 6 <= 9)
    [3,6] -> (3 + 6 <= 9)
    Example 2:

    Input: nums = [3,3,6,8], target = 10
    Output: 6
    Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
    [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
    Example 3:

    Input: nums = [2,3,3,4,6,7], target = 12
    Output: 61
    Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
    Number of valid subsequences (63 - 2 = 61).
    

    Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    1 <= target <= 10^6
'''

expPow = [1]*(10**5)

class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        n, M = len(nums), 10**9+7
        mul, add = lambda x,y: (x%M * y%M)%M, lambda x,y: (x%M + y%M)%M
        
        def exp(base:int,pow:int):
            res=expPow[pow]
            if res == 1:
                while pow>0:
                    if pow&1: res = mul(res, base)
                    base = mul(base,base)
                    pow>>=1
                expPow[pow]=res
            return res
        
        nums.sort()
        
        def binarySearch(l:int,lmt:int): 
            r=n-1
            #find 'i' such that nums[i] > nums[l] and nums[i] < lmt, 'i' is most farthest from 'l'
            while l<r:#l always a true value
                m = (r+l+1)//2
                if nums[m] > lmt:
                    r = m-1
                else:
                    l = m
            return l
        
        res=0
        for l, mn in enumerate(nums):
            mx = target-mn
            if mn<=mx:
                r = binarySearch(l, mx)
                res = add(res, exp(2,r-l))

        return res