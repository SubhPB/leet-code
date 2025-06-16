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
from collections import deque

class Solution:
    def specialTriplets(nums:list[int]):
        n = len(nums)
        indexes:dict[int, deque[int]] = {}
        prefix:dict[int, int] = {}
        res, M = 0, 10**9+7
        
        ADD:int = lambda x,y: (x%M+y%M)%M
        MUL:int = lambda x,y: ((x%M)*(y%M))%M

        def bs(inp:list[int],i:int):# return the most nearest index of value which is less than 'i'.
            if not len(inp) or inp[0]>=i: return -1
            l, r = 0, len(inp)-1
            while l<r:
                mid = (l+r)//2
                if inp[mid]>=i:
                    r = mid-1
                else: # mid can be valid output
                    l = mid
            return l

        for x in range(n-1, -1, -1):
            num = nums[x]
            if num not in indexes: indexes[num] = deque()

            if (not (num&1)) and len(indexes[num]): #isEven: can act as (I,K)
                J = num//2
                prev_x = indexes[num][0]

                prev_j = bs(
                    indexes[J] if J in indexes else [],
                    prev_x
                )

                #How many times j has occurred before the prev_j index
                occ_j = prev_j+1 if prev_j!=-1 else 0

                #How many times curr value has occurred excluding now
                occ_x = len(indexes[num])

                prev_prefix = prefix.get(num, 0)
                res -= prev_prefix

                if num==0:
                    prefix[num] = ADD(
                        prev_prefix, occ_x if occ_x>1 else 0
                    )
                else:
                    prefix[num] = ADD(
                        prev_prefix, MUL(occ_x, occ_j)
                    )

                res = ADD(res, prefix[num])
                
            indexes[num].appendleft(x)
        print(f'prefix={prefix} indexes={indexes}')
        
        return res
    
if __name__ == '__main__':
    TestCases = [
        [[6,3,6],1],
        [[0,1,0,0], 1],
        [[8,4,2,8,4], 2]
    ]
    for testcase in TestCases:
        [nums, expected] = testcase
        print(nums)
        ans = Solution.specialTriplets(nums)
        print(f'Nums={nums} Ans={ans} Expected={expected} Test {'PASSED' if ans==expected else 'FAILED'}!')