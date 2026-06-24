class Solution:
    '''
    3937. Minimum Operations to Make Array Modulo Alternating I

    You are given an integer array nums and an integer k.
    In one operation, you can increase or decrease any element of nums by 1.
    An array is called modulo alternating if there exist two distinct integers x and y (0 <= x, y < k) such that:
    For every even index i, nums[i] % k == x
    For every odd index i, nums[i] % k == y
    Return the minimum number of operations required to make nums modulo alternating.

    Example 1:
    Input: nums = [1,4,2,8], k = 3
    Output: 2
    Explanation:
    Let's choose x = 1 for even indices and y = 2 for odd indices.
    Perform the following operations:
    Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8].
    Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8].
    Now, for even indices, nums[i] % k = 1, and for odd indices, nums[i] % k = 2.
    Thus, the total number of operations required is 2.

    Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 10**9
    2 <= k <= 100
    '''
    def minOperations(self, nums: list[int], k: int) -> int:
        res=None; n=len(nums)
        for x in range(k):
            for y in range(x+1,k):
                temp1=0;temp2=0
                for i,num in enumerate(nums):
                    if i%2:
                        temp1+=abs(x-num%k)
                        temp2+=abs(y-num%k)
                    else:
                        temp2+=abs(x-num%k)
                        temp1+=abs(y-num%k)
                if res is None: res=temp1
                res=min(res,temp1,temp2)
        res = 0 if res is None else res
        return res 