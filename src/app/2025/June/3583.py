'''
 * 3583. Count Special Triplets

    You are given an integer array nums.

    A special triplet is defined as a triplet of indices (i, j, k) such that:

    0 <= i < j < k < n, where n = nums.length
    nums[i] == nums[j] * 2
    nums[k] == nums[j] * 2
    Return the total number of special triplets in the array.

    Since the answer may be large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [6,3,6]

    Output: 1

    Explanation:

    The only special triplet is (i, j, k) = (0, 1, 2), where:

    nums[0] = 6, nums[1] = 3, nums[2] = 6
    nums[0] = nums[1] * 2 = 3 * 2 = 6
    nums[2] = nums[1] * 2 = 3 * 2 = 6
    Example 2:

    Input: nums = [0,1,0,0]

    Output: 1

    Explanation:

    The only special triplet is (i, j, k) = (0, 2, 3), where:

    nums[0] = 0, nums[2] = 0, nums[3] = 0
    nums[0] = nums[2] * 2 = 0 * 2 = 0
    nums[3] = nums[2] * 2 = 0 * 2 = 0
    Example 3:

    Input: nums = [8,4,2,8,4]

    Output: 2

    Explanation:

    There are exactly two special triplets:

    (i, j, k) = (0, 1, 3)
    nums[0] = 8, nums[1] = 4, nums[3] = 8
    nums[0] = nums[1] * 2 = 4 * 2 = 8
    nums[3] = nums[1] * 2 = 4 * 2 = 8
    (i, j, k) = (1, 2, 4)
    nums[1] = 4, nums[2] = 2, nums[4] = 4
    nums[1] = nums[2] * 2 = 2 * 2 = 4
    nums[4] = nums[2] * 2 = 2 * 2 = 4
    

    Constraints:

    3 <= n == nums.length <= 105
    0 <= nums[i] <= 105
    python ./src/app/2025/June/3583.py
'''
import math
from collections import deque

class Solution:
    def specialTriplets(nums:list[int]):
        n, res= len(nums), 0
        M = 10**9+7

        indexes:dict[int, deque[int]] = {}
        prefix:dict[int, int] = {}
        dp:dict[int, int] = {}

        ADD:int = lambda x,y: (x%M+y%M)%M
        MUL:int = lambda x,y: ((x%M)*(y%M))%M

        def binarySearch(inp:list[int],i:int,default=-1):
        # return the most nearest index of value which is less than 'i'.
            if len(inp) and inp[0]<i:
                l,r = 0, len(inp)-1
                while l<r:
                    mid = math.ceil((l+r)/2)
                    if inp[mid]>=i:
                        r = mid-1
                    else:
                        l = mid
                return l
            return default

        for x in range(n-1, -1, -1):
            num, J = nums[x], nums[x]//2

            if num not in indexes: indexes[num] = deque()
            
            if len(indexes[num]) and not num&1:
                #We can only form a triplet when I/K is even
                prev_x = indexes[num][0] #When did last curr num occurred

                #prev_j is index of indexes[J] where indexes[J] is the index of nums where J has occurred just before prev num value
                prev_j = binarySearch(
                    indexes[J] if J in indexes else [],
                    prev_x
                ) if num!=0 else len(indexes[num])-2# Remember prev_j is index in indexes[J] not the actual index pointing to nums, indexes[J] points to actual index of nums


                cnt_j = max(0, prev_j+1)#How many times J has occurred before the prev num
                prev_prefix = prefix.get(num, 0)
                res -= prev_prefix

                #How many times num has occurred behind J
                cnt_x = len(indexes[num]) if num!=0 else 1

                #This should also perfectly handle the case like 6636 when no 3 occurred before 636
                dp[num] = ADD(dp.get(num, 0), MUL(cnt_j, cnt_x))
                prefix[num] = ADD(prefix.get(num, 0), dp[num])
                res = ADD(res, prefix[num])

            indexes[num].appendleft(x)

        return res
    
if __name__ == '__main__':
    TestCases = [
        [[6,3,6],1],
        [[0,1,0,0], 1],
        [[8,4,2,8,4], 2],
    ]
    for testcase in TestCases:
        [nums, expected] = testcase
        print(nums)
        ans = Solution.specialTriplets(nums)
        print(f'Nums={nums} Ans={ans} Expected={expected} Test {'PASSED' if ans==expected else 'FAILED'}!')