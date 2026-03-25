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
            
                
