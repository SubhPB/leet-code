import math
class Solution:
    '''
    4039. Sum of Decoded Numbers

    You are given an integer array nums.
    Each nums[i] is an encoded integer representing two positive integers xi and yi. To decode nums[i], define:
    widthi = nums[i] % 10.
    di = floor(nums[i] / 10).
    xi as the integer formed by the first widthi digits of the decimal representation of di.
    yi as the integer formed by all remaining digits of the decimal representation of di.
    It is guaranteed that the decimal representation of di contains more than widthi digits. Therefore, both xi and yi contain at least one digit.
    The decoded value of nums[i] is xiyi.
    Return the sum of the decoded values of all elements in nums, modulo 109 + 7.
    The floor() function returns the integer part of the division.

    Example 1:
    Input: nums = [231]
    Output: 8
    Explanation:
    For 231, we have width = 1, d = 23, x = 2, and y = 3.
    The decoded value of 231 is 23 = 8.
    Since there is only one element in nums, the sum of the decoded values is 8.

    Constraints:
    1 <= nums.length <= 10**5
    100 < nums[i] < 10**15
    1 <= widthi <= 9
    1 <= xi, yi < 10**9
    The digit sequences used to form xi and yi do not have leading zeros.
    It is guaranteed that every element in nums is a valid encoded integer.
    '''
    def sumDecoded(self, nums: list[int]) -> int:
        mod=10**9+7; res=0
        for num in nums:
            w=num%10; d=num//10
            n=1+math.floor(math.log10(d))
            p=n-w
            x=d//pow(10,p,mod)
            y=d%pow(10,p,mod)
            res=(res+pow(x,y,mod))%mod
        return res
    '''
    4040. Minimum Operations to Form Subset Sum I

    You are given an integer array nums and an integer sum.
    In one operation, choose an element with current value x and replace it with either 2 * x or floor(x / 2).
    For each element, all multiplication operations performed on it must occur before any division operations performed on it.
    Return the minimum number of operations needed so that some subset of the resulting array has a sum exactly equal to sum. If it is impossible, return -1.
    The floor() function returns the integer part of the division.

    Example 1:
    Input: nums = [5,6,10], sum = 4
    Output: 3

    Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 500
    1 <= sum <= 5000
    '''
    def minOperations(self, nums: list[int], E: int) -> int:
        #incomplete
        inf=10**18
        n=len(nums)
        dp=[inf for x in range(E+1)]
        dp[0]=0
        res=inf
        for i in range(n-1,-1,-1):
            temp=[inf]*(E+1)
            temp[0]=0
            t=0; x=nums[i]
            while x<=E:
                for y in range(E-x+1):
                    en=y+x
                    temp[en]=min(temp[en],t+dp[y])
                x*=2
                t+=1
            t=1; x=nums[i]//2
            while x>0:
                for y in range(E-x+1):
                    en=y+x
                    temp[en]=min(temp[en],t+dp[y])
                x//=2
                t+=1
            res=min(res,temp[E])
            dp=[*temp]
        return res if res<inf else -1