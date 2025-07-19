'''
2163. Minimum Difference in Sums After Removal of Elements

    You are given a 0-indexed integer array nums consisting of 3 * n elements.

    You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

    The first n elements belonging to the first part and their sum is sumfirst.
    The next n elements belonging to the second part and their sum is sumsecond.
    The difference in sums of the two parts is denoted as sumfirst - sumsecond.

    For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
    Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
    Return the minimum difference possible between the sums of the two parts after the removal of n elements.

    

    Example 1:

    Input: nums = [3,1,2]
    Output: -1
    Explanation: Here, nums has 3 elements, so n = 1. 
    Thus we have to remove 1 element from nums and divide the array into two equal parts.
    - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
    - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
    - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
    The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
    Example 2:

    Input: nums = [7,9,5,8,1,3]
    Output: 1
    Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
    If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
    To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
    It can be shown that it is not possible to obtain a difference smaller than 1.
    

    Constraints:

    nums.length == 3 * n
    1 <= n <= 10^5
    1 <= nums[i] <= 10^5

    python ./src/app/2025/July/2163.py
'''


import heapq
class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        N, n = len(nums), len(nums)//3

        sums = [0, 0]
        leftH, rightH = [], []

        rightPush = lambda x: heapq.heappush(rightH, x)
        rightPop = lambda: heapq.heappop(rightH)

        leftPush = lambda x:heapq.heappush(leftH, -x)
        leftPop = lambda: -heapq.heappop(leftH)

        left, right = [], []

        for i in range(N-n):
            leftPush(nums[i])
            sums[0] += nums[i]
            if len(leftH)>n: sums[0] -= leftPop()
            if i>=n-1: left.append(sums[0])

        for j in range(N-1, n-1, -1):
            rightPush(nums[j])
            sums[1] += nums[j]
            if len(rightH)>n: sums[1] -= rightPop()
            if j<=N-n: right.append(sums[1])

        res = float('inf')
        for i in range(N-2*n+1):
            res = min(
                res, left[i] - right[N-2*n-i]
            )
        return res
        

if __name__ == "__main__":
    testcases = []
    add = lambda nums: testcases.append(nums)

    add(nums = [3,1,2])
    add(nums=[7,9,5,8,1,3])

    for nums in testcases:
        print(f'nums={nums} sol={Solution().minimumDifference(nums)}')
