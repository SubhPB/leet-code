class Solution:
    '''
    3979. Maximum Valid Pair Sum
    You are given an integer array nums of length n and an integer k.
    A pair of indices (i, j) is called valid if:
    0 <= i < j < n
    j - i >= k
    Return the maximum value of nums[i] + nums[j] among all valid pairs.

    Example 1:
    Input: nums = [1,3,5,2,8], k = 2
    Output: 13

    Constraints:
    2 <= n == nums.length <= 10**5
    1 <= nums[i] <= 10**9
    1 <= k <= n - 1
    '''
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n=len(nums); mxr=[0]*n; res=0
        for i,num in enumerate(nums):
            mxr[i]=max(mxr[i-1],num)
        for j in range(n-1,k-1,-1):
            res=max(res,nums[j]+mxr[j-k])
        return res
    '''
    3980. Minimum Operations to Transform Binary String

    You are given two binary strings s1 and s2 of the same length n.
    You can perform the following operations on s1 any number of times, in any order:
    Choose an index i such that s1[i] == '0', and change it to '1'.
    Choose an index i such that 0 <= i < n - 1, and both s1[i] and s1[i + 1] are '1'. Change both characters to '0'.
    Return the minimum number of operations required to make s1 equal to s2. If it is impossible, return -1.

    Example 1:
    Input: s1 = "11", s2 = "00"
    Output: 1
    Explanation:
    Change indices 0 and 1 from '1' to '0' in one operation, so "11" becomes "00". Thus, the answer is 1.

    Constraints:
    1 <= n == s1.length == s2.length <= 10**5
    s1 and s2 consist only of '0' and '1'.
    '''
    def minOperations(self, s1: str, s2: str) -> int:
        n=len(s1)
        score=[0]*(n+2)
        inf=10**18
        def do_op1(i:int):
            if s1[i]==s2[i]:
                return 0
            if not int(s1[i]):
                return 1
            return inf
        ops=[
            [0,1,1,2],
            [2,0,3,1],
            [2,3,0,1],
            [1,2,2,0]
        ]
        def do_op2(i:int):
            # comprise [i]-ème et [i+1]-ème
            return ops[int(s1[i:i+2],2)][int(s2[i:i+2],2)]

        score[n-1]=do_op1(n-1)
        for i in range(n-2,-1,-1):
            score[i]=min(
                score[i+1]+do_op1(i),
                score[i+2]+do_op2(i),
                score[i+1]+do_op2(i)
            )
        if score[0]>=inf:
            return -1
        return score[0]
    '''
    3981. Count Distinct Ways to Form Target from Two Strings

    You are given three strings word1, word2, and target.
    Your task is to count the number of ways to form target by choosing characters from word1 and word2 under the following conditions:
    For each character of target, choose one matching character from either word1 or word2.
    The chosen indices from word1 must be strictly increasing.
    The chosen indices from word2 must be strictly increasing.
    At least one character must be chosen from both word1 and word2.
    Two ways are considered different if, for at least one position in target, the chosen character comes from a different string or a different index.
    Return the number of ways. Since the answer may be very large, return it modulo 109 + 7.

    Example 1:
    Input: word1 = "abc", word2 = "bac", target = "abc"
    Output: 5

    Explanation:
    There are 5 ways to form target:
    word1[0] = 'a', word1[1] = 'b', word2[2] = 'c'
    word1[0] = 'a', word2[0] = 'b', word1[2] = 'c'
    word1[0] = 'a', word2[0] = 'b', word2[2] = 'c'
    word2[1] = 'a', word1[1] = 'b', word1[2] = 'c'
    word2[1] = 'a', word1[1] = 'b', word2[2] = 'c'
    All ways preserve the increasing index order inside each string and choose at least one character from each string.

    Constraints:
    1 <= word1.length, word2.length, target.length <= 100
    word1, word2, and target consist of lowercase English letters only.
    '''
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        pass