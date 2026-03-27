from functools import reduce
from typing import List
from collections import deque
class Solution:
    '''
    3875. Construct Uniform Parity Array I

    You are given an array nums1 of n distinct integers.
    You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.
    For each index i, you must choose exactly one of the following (in any order):
    nums2[i] = nums1[i]
    nums2[i] = nums1[i] - nums1[j], for an index j != i
    Return true if it is possible to construct such an array, otherwise, return false.

    Example 1:
    Input: nums1 = [2,3]
    Output: true
    Explanation:
    Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
    Choose nums2[1] = nums1[1] = 3.
    nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.
 
    Constraints:
    1 <= n == nums1.length <= 100
    1 <= nums1[i] <= 100
    nums1 consists of distinct integers.
    '''
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
    '''
    3876. Construct Uniform Parity Array II
    You are given an array nums1 of n distinct integers.
    You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.
    For each index i, you must choose exactly one of the following (in any order):
    nums2[i] = nums1[i]​​​​​​​
    nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
    Return true if it is possible to construct such an array, otherwise return false.

    Example 1:
    Input: nums1 = [1,4,7]
    Output: true
    Explanation:​​​​​​​​​​​​​​
    Set nums2[0] = nums1[0] = 1.
    Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
    Set nums2[2] = nums1[2] = 7.
    nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.

    Constraints:
    1 <= n == nums1.length <= 10^5
    1 <= nums1[i] <= 10^9
    nums1 consists of distinct integers.
    '''
    def uniformArray(self, nums1: list[int]) -> bool:
        e=0; on=10**9+1; en=10**9
        for num in nums1:
            if num%2: on=min(on,num)
            else:
                e+=1; en=min(en,num)
        return e in [0,len(nums1)] or en>on
    '''
    3877. Minimum Removals to Achieve Target XOR

    You are given an integer array nums and an integer target.
    You may remove any number of elements from nums (possibly zero).
    Return the minimum number of removals required so that the bitwise XOR of the remaining elements equals target. If it is impossible to achieve target, return -1.
    The bitwise XOR of an empty array is 0.

    Example 1:
    Input: nums = [1,2,3], target = 2
    Output: 1
    Explanation:
    Removing nums[1] = 2 leaves [nums[0], nums[2]] = [1, 3].
    The XOR of [1, 3] is 2, which equals target.
    It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.

    Constraints:
    1 <= nums.length <= 40
    0 <= nums[i] <= 10^4
    0 <= target <= 10^4
    '''
    def minRemovals(self, nums: List[int], target: int) -> int:
        target^=reduce(lambda a,b:a^b, nums) 
        if target == 0:  return 0
        queue, seen = deque([0]), {0}                 
        res, n = 1, 1

        while queue:                                    
            for _ in range(n):
                prv = queue.popleft()
                for num in nums:
                    cur = prv ^ num
                    if cur == target: return res        
                    if cur in seen: continue            
                    seen.add(cur)
                    queue.append(cur)
            res += 1
            n = len(queue)

        return -1                                    
    '''
    3878. Count Good Subarrays

    You are given an integer array nums.
    A subarray is called good if the bitwise OR of all its elements is equal to at least one element present in that subarray.
    Return the number of good subarrays in nums.
    Here, the bitwise OR of two integers a and b is denoted by a | b.

    Example 1:
    Input: nums = [4,2,3]
    Output: 4
    Explanation:
    The subarrays of nums are:
    Subarray	Bitwise OR	Present in Subarray
    [4]	4 = 4	Yes
    [2]	2 = 2	Yes
    [3]	3 = 3	Yes
    [4, 2]	4 | 2 = 6	No
    [2, 3]	2 | 3 = 3	Yes
    [4, 2, 3]	4 | 2 | 3 = 7	No
    Thus, the good subarrays of nums are [4], [2], [3] and [2, 3]. Thus, the answer is 4.

    Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    '''
    def countGoodSubarrays(self, nums: list[int]) -> int:
        return -1