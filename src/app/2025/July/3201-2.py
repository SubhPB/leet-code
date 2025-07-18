'''
3201. Find the Maximum Length of Valid Subsequence I
    You are given an integer array nums.
    A subsequence sub of nums with length x is called valid if it satisfies:

    (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
    Return the length of the longest valid subsequence of nums.

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    Example 1:

    Input: nums = [1,2,3,4]

    Output: 4

    Explanation:

    The longest valid subsequence is [1, 2, 3, 4].

    Example 2:

    Input: nums = [1,2,1,1,2,1,2]

    Output: 6

    Explanation:

    The longest valid subsequence is [1, 2, 1, 2, 1, 2].

    Example 3:

    Input: nums = [1,3]

    Output: 2

    Explanation:

    The longest valid subsequence is [1, 3].

    Constraints:

    2 <= nums.length <= 2 * 10^5
    1 <= nums[i] <= 10^7

3202. Find the Maximum Length of Valid Subsequence II
    You are given an integer array nums and a positive integer k.
    A subsequence sub of nums with length x is called valid if it satisfies:

    (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
    Return the length of the longest valid subsequence of nums.
    
    Example 1:

    Input: nums = [1,2,3,4,5], k = 2

    Output: 5

    Explanation:

    The longest valid subsequence is [1, 2, 3, 4, 5].

    Example 2:

    Input: nums = [1,4,2,3,1,4], k = 3

    Output: 4

    Explanation:

    The longest valid subsequence is [1, 4, 1, 4].


    Constraints:

    2 <= nums.length <= 10^3
    1 <= nums[i] <= 1067
    1 <= k <= 10^3
'''

class Solution:
    def maximumLength3201(self, nums):
        n, oddCnt, ratio = len(nums), 0, 0
        for num in nums:
            oddCnt += num%2
            if ratio%2 == num%2: ratio+=1
        if nums[0]&1: ratio+=1 # oddEvenRatio > evenOddRatio
        return max(
            oddCnt,
            n-oddCnt,
            ratio
        )
    def maximumLength3202(self, nums: list[int], k: int) -> int:
        n, mx = len(nums), 2
        for i in range(n):
            if mx >= n-i-1: break
            for j in range(i+1,n):
                num1, num2 = nums[i], nums[j]
                subSeq, l = [num1,num2], 2
                rmod = (num1+num2)%k
                # Using subSeq[0] we can find subSeq[2] same as with subSeq[1] will conclude subSeq[3]
                # for i in range(2):

        return mx