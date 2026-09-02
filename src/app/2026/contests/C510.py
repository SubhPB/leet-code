class Solution:
    '''
    3987. Minimum Total Cost to Process All Elements

    You are given an integer array nums and an integer k.
    Initially, you have k units of resources.
    You must process the elements of nums from left to right. To process the ith element, you need nums[i] resources.
    If your available resources are less than nums[i], you may perform an operation that increases your available resources by k. The value of k is fixed and does not change throughout the process.
    The first such operation incurs a cost of 1, the second incurs a cost of 2, and so on.
    After processing the ith element, your available resources decrease by nums[i].
    Return an integer denoting the minimum total cost required to process all elements. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:
    Input: nums = [1,2,3,4], k = 4
    Output: 3
    Explanation:
    After processing nums[0], we have 4 - 1 = 3 units of resources left.
    After processing nums[1], we have 3 - 2 = 1 unit of resources left.
    Since nums[2] = 3 and only 1 unit of resources is available, we perform the first operation costing 1. After processing nums[2], we have 1 + 4 - 3 = 2 units of resources left.
    Since nums[3] = 4 and only 2 units of resources are available, we perform the second operation costing 2, to have 2 + 4 = 6 units of resources, which is enough to process nums[3].
    Thus, the total cost is 1 + 2 = 3.

    Constraints:
    1 <= nums.length <= 10**5
    1 <= nums[i] <= 10**9
    1 <= k <= 10**9
    '''
    def minimumCost(self, nums: list[int], k: int) -> int:
        mod=10**9+7
        rsrc=k
        ops=0
        mul=lambda x,y: (x%mod*y%mod)%mod
        add=lambda x,y: (x%mod+y%mod)%mod
        for num in nums:
            if num>rsrc:
                f=(num-rsrc+k-1)//k
                ops=add(ops,f)
                rsrc=add(rsrc, mul(f,k))
            rsrc-=num
        return mul(ops,ops+1)//2